#!/usr/bin/env python
import time, datetime, sys, pigpio, config, ephem
import Adafruit_DHT


class Main():

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


        try:
            while True:
                self._run()
                time.sleep(60)
        except:
            self.pi.stop()

    def _get_sunrise_sunset(self):
        print "Calculating today's sunrise and sunset times"
        o=ephem.Observer()
        o.lat = config.latitude
        o.long = config.longitude
        #o.date = datetime.datetime.utcnow()
        #o.date = ephem.localtime(ephem.now())
        s = ephem.Sun()
        s.compute()

        #self.sunrise = o.next_rising(s)
        #self.sunset = o.next_setting(s)

        self.sunrise = ephem.localtime(o.next_rising(s))
        self.sunset = ephem.localtime(o.next_setting(s))

        print "Date: " , ephem.localtime(o.date)
        print "Latitude: %s, Longitude: %s" % (o.lat, o.long)
        print "Sunrise: %s" % self.sunrise
        print "Sunset: %s" % self.sunset

        self.islight = self.sunrise > self.sunset

    def _get_temp_and_humidity(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(self.s, config.th_channel)

        if self.temperature is not None:
            print 'Raw Temperature: {0:0.1f}*C'.format(self.temperature)

            if config.temp_adjustment != 0:
                self.temperature += config.temp_adjustment
                print 'Adjusted Temperature: {0:0.1f}*C'.format(self.temperature)
        else:
            print 'Temperature: not available'

        if self.humidity is not None:
            print 'Humidity: {0:.2f}%'.format(self.humidity)
        else:
            print 'Humidity: not available'


    def _run(self):

        self._get_sunrise_sunset()
        self._get_temp_and_humidity()

        print "Updating Light Show: ", datetime.datetime.now()
        if self.islight:
            print "Currently it's light"
            self._set_rgb_led(r=25, g=75, b=0)
            self._set_white_led(w=25)

        else:
            print "Currently it's Dark"
            self._set_rgb_led(r=0, g=20, b=20)
            self._set_white_led(w=0)
        print ''
        sys.stdout.flush()


    def _set_rgb_led(self, r=0, g=0, b=0):
        self.pi.set_PWM_dutycycle(config.r_channel, r)
        self.pi.set_PWM_dutycycle(config.g_channel, g)
        self.pi.set_PWM_dutycycle(config.b_channel, b)

    def _set_white_led(self, w=0):
        self.pi.set_PWM_dutycycle(config.w_channel, w)


#        time.sleep(2)

# def day():
#     pi.set_PWM_dutycycle(r_channel, 25)
#     pi.set_PWM_dutycycle(g_channel, 75)
#     pi.set_PWM_dutycycle(b_channel, 0)
#     pi.set_PWM_dutycycle(w_channel, 25)
#
# def night():
#     pi.set_PWM_dutycycle(r_channel, 0)
#     pi.set_PWM_dutycycle(g_channel, 20)
#     pi.set_PWM_dutycycle(b_channel, 20)
#     pi.set_PWM_dutycycle(w_channel, 0)
#
# day()
#night()

Main()