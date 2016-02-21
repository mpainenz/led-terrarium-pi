#!/usr/bin/env python
import time, sys, pigpio, config, ephem, timezone


class Main():

    def __init__(self):
        print "Starting Auto LED Controller"
        self.start_time = time.time()

        print "Initializing connection to pigpio daemon"
        # pigpio daemon is required for accurate PWM timing
        self.pi = pigpio.pi()


        self._get_sunrise_sunset()



        while True:
            self._run()
            time.sleep(2)

        self.pi.stop()

    def _get_sunrise_sunset(self):
        print "Loading Todays Sunrise and Sunset times"
        o=ephem.Observer()
        o.lat = config.latitude
        o.long = config.longitude
        # Civil Horizon
        o.horizon = -6
        s = ephem.Sun()
        s.compute()

        print "Latitude: %s, Longitude: %s" % (o.lat, o.long)
        print "Sunrise: %s" % ephem.localtime(o.next_rising(s))
        print "Sunset: %s" % ephem.localtime(o.next_setting(s))

    def _run(self):
        print "Running"




    def _set_rgb_led(self, r=0, g=0, b=0):
        pi.set_PWM_dutycycle(config.r_channel, self._percentage_to_pigpio(r))
        pi.set_PWM_dutycycle(config.g_channel, self._percentage_to_pigpio(g))
        pi.set_PWM_dutycycle(config.b_channel, self._percentage_to_pigpio(b))

    def _set_white_led(self, w=0):
        pi.set_PWM_dutycycle(config.w_channel, self._percentage_to_pigpio(w))

    def _percentage_to_pigpio(self, p=0):
        # 100% = 255
        return p * 2.5

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