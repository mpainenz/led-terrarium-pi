import datetime
import unittest

from terrarium_lights import TerrariumLights


class TerrariumTests(unittest.TestCase):


    def setUp(self):
        print('Started Test')
        self.terrarium_lights = TerrariumLights(test_mode=True)
        now = datetime.datetime.now()
        self.terrarium_lights._get_sunrise_sunset(now)

    def tearDown(self):
        print('Finished Test')


    def test_exactly_sunset(self):
        # Test Exactly next Sunset
        test_time = self.terrarium_lights.sunset
        self.terrarium_lights._update_lighting(test_time)


    def test_sunset_minus_1_minute(self):
        test_time = self.terrarium_lights.sunset - datetime.timedelta(seconds=60)
        self.terrarium_lights._update_lighting(test_time)

    def test_sunset_minus_10_minute(self):
        test_time = self.terrarium_lights.sunset - datetime.timedelta(seconds=600)
        self.terrarium_lights._update_lighting(test_time)


if __name__ == '__main__':
    unittest.main()
