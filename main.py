#!/usr/bin/env python
import config, database
import time, datetime, sys, pigpio, ephem
import Adafruit_DHT
import pygal

class Main():

    demo_time = None # Used instead of current time when in Demo mode

    LOG_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

    # Temp and Humidity
    temperature = None
    humidity = None

    # Date/Time of Sunrise/Sunset
    sunrise = None
    sunset = None

    def __init__(self):
        print "Starting Auto LED Controller"
        self.start_time = time.time()

        print "Initializing connection to pigpio daemon"
        # pigpio daemon is required for accurate PWM timing
        self.pi = pigpio.pi()

        print "Initializing Temp/Humidity sensor"
        # Sensor should be set to Adafruit_DHT.DHT11,
        # Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
        self.s = config.sensor

        if config.DEMO_MODE:
            print "Running in Demo Mode"
            self.demo_time = datetime.datetime.now()
            self._get_sunrise_sunset(self.demo_time)
            # Go to the start of Sunset
            self.demo_time = self.sunrise - datetime.timedelta(0, config.sunrise_colour_map.keys()[0])
        else:
            print "Building DB if required"
            database.build_tables()

        #try:
        while True:
            if config.DEMO_MODE:
                self._run(self.demo_time)
                self.demo_time = self.demo_time + datetime.timedelta(0, config.DEMO_SPEED)
                time.sleep(1)
            else:
                self._run(datetime.datetime.now())
                time.sleep(60)
        # except Exception as e:
        #     self.pi.stop()
        #     print 'Error: ', e.message

    def _run(self, now):
        print 'Running: ', self._timestamp(now)
        self._get_sunrise_sunset(now)
        if not config.DEMO_MODE:
            if self._get_temp_and_humidity():
                self._save_to_db(self.temperature, self.humidity)
                self._update_graphs()
        self._update_lighting(now)
        print ''
        sys.stdout.flush()

    def _get_sunrise_sunset(self, now):

        if None in (self.sunrise, self.sunset)\
                or now > self.sunrise\
                or now > self.sunset:

            print "Calculating sunrise and sunset times"
            o = ephem.Observer()
            if config.DEMO_MODE:
                o.date = now - (datetime.datetime.now() - datetime.datetime.utcnow()) # ephem uses UTC Time
            o.lat = config.latitude
            o.long = config.longitude
            s = ephem.Sun()
            s.compute()

            self.sunrise = ephem.localtime(o.next_rising(s))
            self.sunset = ephem.localtime(o.next_setting(s))

            print "Date: " , ephem.localtime(o.date)

            print "Latitude: %s" % o.lat
            print "Longitude: %s" % o.long
            print "Sunrise: %s" % self._timestamp(self.sunrise)
            print "Sunset: %s" % self._timestamp(self.sunset)

    def _update_lighting(self, now):

        def get_start_colour_from_map(delta, colour_map):
            delta_result, colour_result = None, None
            for d, c in colour_map.iteritems():
                if delta < d:
                    delta_result, colour_result = d, c
            return delta_result, colour_result

        def get_end_colour_from_map(delta, colour_map):
            for d, c in colour_map.iteritems():
                if delta < d:
                    return d, c
            return None, None

        def get_blend_percentage(delta, start_delta, end_delta):
            diff = start_delta - end_delta
            if diff == 0:
                return 0
            v = delta - start_delta
            return (v / diff) * 100


        self.islight = self.sunrise > self.sunset

        blending_required = False
        if self.islight:
            effective_colour = config.day_colour

            delta = (self.sunset - now).total_seconds()
            start_delta, start_colour = get_start_colour_from_map(delta, config.sunrise_colour_map)
            if start_delta is not None:
                blending_required = True
                effective_colour = list(start_colour)
                end_delta, end_colour = get_end_colour_from_map(delta, config.sunrise_colour_map)
            else:
                print "Currently it's daytime, %f seconds until sunset starts" % delta

        else:
            effective_colour = config.night_colour
            delta = (self.sunrise - now).total_seconds()
            start_delta, start_colour = get_start_colour_from_map(delta, config.sunrise_colour_map)
            if start_delta is not None:
                blending_required = True
                effective_colour = start_colour
                end_delta, end_colour = get_end_colour_from_map(delta, config.sunrise_colour_map)
            else:
                print "Currently it's Dark, %f seconds until sunrise" % delta

        if blending_required:
            blend_percentage = get_blend_percentage(delta, start_delta, end_delta)

            def blend_colour(start_value, end_value, blend_percentage):
                diff = end_value - start_value
                if diff > 0:
                    return start_value + ((diff / 100) * blend_percentage)
                else:
                    return start_value

            effective_colour = list(effective_colour)
            effective_colour[0] = blend_colour(start_colour[0], end_colour[0], blend_percentage)
            effective_colour[1] = blend_colour(start_colour[1], end_colour[1], blend_percentage)
            effective_colour[2] = blend_colour(start_colour[2], end_colour[2], blend_percentage)
            effective_colour[3] = blend_colour(start_colour[3], end_colour[3], blend_percentage)



        self._set_rgb_led(r=effective_colour[0], g=effective_colour[1], b=effective_colour[2])
        self._set_white_led(w=effective_colour[3])

    def _get_temp_and_humidity(self):
        print "Polling Temperature/Humidity Sensor"
        # Get latest readings from sensor. May return None if a CRC error was encountered
        h, t = Adafruit_DHT.read_retry(self.s, config.th_channel)

        # Check that values were retrieved, and are in range
        valid = None not in (h, t) and 0 < h < 100

        # If a previous value was saved, check that the new values are not wildly different
        if valid and None not in (self.humidity, self.temperature):

            if config.humidity_delta_threshold:
                h_delta = abs(self.humidity - h)
                valid = h_delta < config.humidity_delta_threshold
                if not valid:
                    print "humidity exceeded delta threshold"

            if valid and config.temp_delta_threshold:
                t_delta = abs(self.temperature - t)
                valid = t_delta < config.temp_delta_threshold
                if not valid:
                    print "Temperature exceeded delta threshold"

        if valid:
            print 'Humidity: {0:.2f}%'.format(h)
            print 'Temperature: {0:0.1f}*C'.format(t)
            if config.temp_adjustment != 0:
                t += config.temp_adjustment
                print 'Adjusted Temperature: {0:0.1f}*C'.format(t)

            self.humidity = h
            self.temperature = t

        else:
            print 'Temperature/Humidity not available'



        return None not in (self.temperature, self.humidity)

    def _save_to_db(self, temperature, humidity):
        print "Saving to DB"
        reading = database.SensorReading()
        reading.humidity = self.humidity
        reading.temperature = self.temperature
        reading.snapshotDate = datetime.datetime.now()
        database.session.add(reading)
        try:
            database.session.commit()
        except Exception as e:
            print e.message

    def _update_graphs(self):
        print "Generating Graph"
        line_chart = pygal.Line()
        line_chart.title = "test"

        temps = []
        humidities = []
        dates = []


        # Get Todays Graph
        start_of_day = datetime.datetime.now()
        start_of_day = start_of_day.replace(hour=0, minute=0, second=0, microsecond=0)

        sensor_readings = database.session.query(database.SensorReading)\
            .filter(database.SensorReading.snapshotDate > start_of_day)\
            .order_by(database.SensorReading.snapshotDate)\
            .all()

        for r in sensor_readings:
            dates.append(r.snapshotDate)
            temps.append(r.temperature)
            humidities.append(r.humidity)

        line_chart.x_labels = dates
        line_chart.add('Temperature', temps)
        line_chart.add('Humidity', humidities)
        line_chart.render_to_file('test.svg')



    def _set_rgb_led(self, r=0, g=0, b=0):
        self.pi.set_PWM_dutycycle(config.r_channel, r)
        self.pi.set_PWM_dutycycle(config.g_channel, g)
        self.pi.set_PWM_dutycycle(config.b_channel, b)

    def _set_white_led(self, w=0):
        self.pi.set_PWM_dutycycle(config.w_channel, w)

    def _timestamp(self, value=None):
        if value == None:
            value = datetime.datetime.now()
        return datetime.datetime.strftime(value, self.LOG_TIME_FORMAT)


Main()