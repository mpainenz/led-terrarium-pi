import Adafruit_DHT

# GPIO Channel for RGB LED Strip
r_channel = 17
g_channel = 27
b_channel = 22

# GPIO Channel for white LED Strip
w_channel = 18

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
sensor = Adafruit_DHT.AM2302

# Optionally specify an amount in Degrees to adjust the output temperature by.
# Useful if the sensor is slightly out, which is not uncommon
temp_adjustment = -2.0

# GPIO Channel for Temperature & Humidity Sensor
th_channel = 23

# Location Latitude and Longitude (Auckland, New Zealand)
latitude = "-36.84"
longitude = "174.74"

