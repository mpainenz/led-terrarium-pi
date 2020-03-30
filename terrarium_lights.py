import collections
import sys
import config
import time, datetime, pigpio
from datetime import timedelta
import argparse
import ephem


# Debug statements to help diagnose issues when Python wont run this script
# print(sys.executable)
# import os
# print(os.getcwd())
# print(sys.path)
# import platform
# print(platform.python_version())


class TerrariumLights:
    demo_time = None  # Used instead of current time when in Demo mode

    LOG_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

    # Temp and Humidity
    temperature = None
    humidity = None

    # Date/Time of Sunrise/Sunset
    previous_sunrise = None
    sunrise = None
    sunset = None

    def __init__(self, test_mode=False):

        self.test_mode = test_mode

        # Parse Aruments
        parser = argparse.ArgumentParser(description='Service to control LED Lighting in a Terrarium')
        parser.add_argument("r", nargs='?', default=0)
        parser.add_argument("g", nargs='?', default=0)
        parser.add_argument("b", nargs='?', default=0)
        parser.add_argument("w", nargs='?', default=0)
        args = parser.parse_args()

        print "Starting Auto LED Controller"
        self.start_time = time.time()

        print "Initializing connection to pigpio daemon"
        # pigpio daemon is required for accurate PWM timing
        if not self.test_mode:
            self.pi = pigpio.pi()

        if any(x > 0 for x in (args.r, args.g, args.b, args.w)):
            self._set_rgb_led(r=args.r, g=args.g, b=args.b)
            self._set_white_led(w=args.w)
            time.sleep(0.5)
            self.pi.stop()
            # time.sleep(3)
            sys.exit(0)

        print "Initializing Temp/Humidity sensor"
        # Sensor should be set to Adafruit_DHT.DHT11,
        # Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.

        # self.s = config.sensor

        if config.DEMO_MODE:
            print "Running in Demo Mode"
            self.demo_time = datetime.datetime.now()
            self._get_sunrise_sunset(self.demo_time)
            # Go to the start of Sunset
            self.demo_time = self.sunrise - datetime.timedelta(0, config.sunrise_colour_map.keys()[0])

        # try:
        while True and not self.test_mode:
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
        # if not config.DEMO_MODE:
        # if self._get_temp_and_humidity():
        #    if config.ENABLE_DB:
        #        self._save_to_db(self.temperature, self.humidity)
        #    #self._update_graphs()
        self._update_lighting(now)
        print ''
        sys.stdout.flush()

    def _get_sunrise_sunset(self, now):

        if None in (self.sunrise, self.sunset) \
                or now > self.sunrise \
                or now > self.sunset:

            print "Calculating sunrise and sunset times"
            o = ephem.Observer()
            # o.horizon = -6 #http://rhodesmill.org/pyephem/rise-set.html#naval-observatory-risings-and-settings
            if config.DEMO_MODE:
                o.date = now - (datetime.datetime.now() - datetime.datetime.utcnow())  # ephem uses UTC Time
            o.lat = config.latitude
            o.long = config.longitude
            s = ephem.Sun()
            s.compute()

            try:
                self.last_sunrise = ephem.localtime(o.previous_rising(s))
            except (ephem.AlwaysUpError, ephem.NeverUpError):
                print 'got that damn error'
                pass

            self.sunrise = ephem.localtime(o.next_rising(s))

            self.sunrise += timedelta(
                hours=1)  # Terrarium was bright too early. Sunrise calculation may be slightly out, potentially an issue with how Sunrise is calculated versus what a person on the ground sees. IE Actual Astronomical Sunrise may be calculated from the moment the sun is in position, rather than when the sunrise looks to be happening.

            self.sunset = ephem.localtime(o.next_setting(s))

            print "Date: ", ephem.localtime(o.date)

            print "Latitude: %s" % o.lat
            print "Longitude: %s" % o.long
            print "Previous Sunrise: %s" % self._timestamp(self.previous_sunrise)
            print "Next Sunrise: %s" % self._timestamp(self.sunrise)
            print "Next Sunset: %s" % self._timestamp(self.sunset)

    def _update_lighting(self, effective_time):
        is_light = self.sunrise > self.sunset
        if is_light:
            effective_colour = config.day_colour
            current_phase, next_phase = 'day', 'sunset'
            delta = (self.sunset - effective_time).total_seconds()
            colour_map = config.sunset_colour_map
        else:
            effective_colour = config.night_colour
            current_phase, next_phase = 'night', 'sunrise'
            delta = (self.sunrise - effective_time).total_seconds()
            colour_map = config.sunrise_colour_map

        print "Currently ", current_phase

        start_delta, start_colour = self.get_start_colour_from_map(delta, colour_map)
        if start_delta is not None:
            blending_required = True
            effective_colour = start_colour
            end_delta, end_colour = self.get_end_colour_from_map(delta, colour_map)
        else:
            blending_required = False
            end_delta = None
            end_colour = None
            print "%s in %d seconds" % (next_phase, delta)

        if blending_required:
            blend_percentage = self.get_blend_percentage(delta, start_delta, end_delta)
            effective_colour = self.blend_colours(start_colour, end_colour, blend_percentage)
            print "Blend Percentage: ", blend_percentage
            print "Start Colour: ", start_colour
            print "End Colour: ", end_colour

        print "Current Delta: ", delta
        print "Start Delta: ", start_delta
        print "End Delta: ", end_delta
        print "Effective Colour: ", effective_colour

        # Update LEDs
        if (effective_colour[0] >= 0) and (effective_colour[1] >= 0) and (effective_colour[2] >= 0) and (
                effective_colour[3] >= 0):
            self._set_rgb_led(r=effective_colour[0], g=effective_colour[1], b=effective_colour[2])
            self._set_white_led(w=effective_colour[3])

    def get_start_colour_from_map(self, delta, colour_map):
        delta_result, colour_result = None, None

        sorted_colour_map = collections.OrderedDict(sorted(colour_map.items()))

        for d, c in sorted_colour_map.iteritems():
            if delta <= d:
                delta_result, colour_result = d, c
        return delta_result, colour_result

    def get_end_colour_from_map(self, delta, colour_map):
        sorted_colour_map = collections.OrderedDict(sorted(colour_map.items()))
        for d, c in sorted_colour_map.iteritems():
            if delta >= d:
                return d, c
        return None, None

    def get_blend_percentage(self, delta, start_delta, end_delta):
        diff = start_delta - end_delta
        if diff == 0:
            return 0
        v = start_delta - delta
        blended = (v / diff) * 100
        if blended > 0:
            return (v / diff) * 100
        else:
            return 0

    def blend_colours(self, start_colour, end_colour, blend_percentage):
        print "Blend Percentage: ", blend_percentage
        blended_colour = [0, 0, 0, 0]
        for i in range(4):
            diff = end_colour[i] - start_colour[i]
            print "diff: ", diff
            if diff != 0:
                test = diff / 100
                # print "test: ", test
                blend_shift = ((diff / 100) * blend_percentage)
                # print "Blend Shift: ", blend_shift
                blended_colour[i] = start_colour[i] + blend_shift
            else:
                blended_colour[i] = start_colour[i]
        print "Blend Test: ", blended_colour
        return blended_colour

    def _set_rgb_led(self, r=0, g=0, b=0):
        if not self.test_mode:
            self.pi.set_PWM_dutycycle(config.r_channel, r)
            self.pi.set_PWM_dutycycle(config.g_channel, g)
            self.pi.set_PWM_dutycycle(config.b_channel, b)

    def _set_white_led(self, w=0):
        if not self.test_mode:
            self.pi.set_PWM_dutycycle(config.w_channel, w)

    def _timestamp(self, value=None):
        if value == None:
            value = datetime.datetime.now()
        return datetime.datetime.strftime(value, self.LOG_TIME_FORMAT)
