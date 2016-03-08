#!/usr/bin/env python
import time, datetime, sys, pigpio, config, ephem
import Adafruit_DHT

class Main():

    DEMO_MODE = False # Fast forward mode
    DEMO_SPEED = 60 #1 sec = x sec

    demo_time = None # Used instead of current time when in Demo mode

    LOG_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

    # Date/Time of Sunrise/Sunset
    sunrise = None
    sunset = None


    # {-3600,      0,      0,      0},
    # {-3000,      0,      0,    200}, // Dark blue
    # {-2400,    500,    200,    500},
    # {-1800,   1000,    200,    500}, // Sun begins to rise
    # {-1500,   2000,   1000,    500},
    # {-1200,   5000,   3000,    500}, // Yellowish
    # { -900,   6000,   4000,   2000}, // White
    # {    0,  10000,   7000,   4000}, // Bright white
    # { 3300,  10000,   7000,   4000}, // Begin to fade off

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

        if self.DEMO_MODE:
            print "Running in Demo Mode"
            self.demo_time = datetime.datetime.now()

        try:
            while True:
                if self.DEMO_MODE:
                    self._run(self.demo_time)
                    self.demo_time = self.demo_time + datetime.timedelta(0,self.DEMO_SPEED)
                    time.sleep(1)
                else:
                    self._run(datetime.datetime.now())
                    time.sleep(60)
        except:
            self.pi.stop()

    def _run(self, now):
        print 'Running: ', self._timestamp(now)
        self._get_sunrise_sunset(now)
        if not self.DEMO_MODE:
            self._get_temp_and_humidity()
        self._update_lighting(now)
        print ''
        sys.stdout.flush()

    def _get_sunrise_sunset(self, now):

        if None in (self.sunrise, self.sunset)\
                or now > self.sunrise\
                or now > self.sunset:

            print "Calculating sunrise and sunset times"
            o = ephem.Observer()
            o.date = now
            o.lat = config.latitude
            o.long = config.longitude
            s = ephem.Sun()
            s.compute()

            self.sunrise = ephem.localtime(o.next_rising(s))
            self.sunset = ephem.localtime(o.next_setting(s))

            #print "Date: " , ephem.localtime(o.date)
            print "Latitude: %s" % o.lat
            print "Longitude: %s" % o.long
            print "Sunrise: %s" % self._timestamp(self.sunrise)
            print "Sunset: %s" % self._timestamp(self.sunset)

    def _update_lighting(self, now):
        self.islight = self.sunrise > self.sunset

        if self.islight:
            print "Currently it's light"
            self._set_rgb_led(r=25, g=75, b=0)
            self._set_white_led(w=25)

        else:
            print "Currently it's Dark"
            self._set_rgb_led(r=0, g=20, b=20)
            self._set_white_led(w=0)


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