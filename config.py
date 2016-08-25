import Adafruit_DHT

# Set to true to run through Sunrise colours in Demo mode
DEMO_MODE = False # Fast forward mode
DEMO_SPEED = 10 #1 sec = x sec

# GPIO Channel for RGB LED Strip
r_channel = 25
g_channel = 27
b_channel = 22

# GPIO Channel for white LED Strip
w_channel = 18

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.
# For AM2301, specify AM2302
sensor = Adafruit_DHT.AM2302

# Optionally specify an amount in Degrees to adjust the output temperature by.
# Useful if the sensor is slightly out, which is not uncommon
temp_adjustment = 0

# Optionally set a valid threshold delta that a new reading must not pass to be valid. Useful if you occasionally get
# invalid values from your temp/humidity sensor. 0 to disable.
temp_delta_threshold = 30 # must not vary X degrees since last reading
humidity_delta_threshold = 50 # must not vary X percent humidity since last reading

# GPIO Channel for Temperature & Humidity Sensor
th_channel = 23

# Location Latitude and Longitude (Auckland, New Zealand)
latitude = "-36.84"
longitude = "174.74"


# RGBW Value to use during Day
day_colour = [75, 255, 0, 100]

# RGBW Value to use during Night
night_colour = [0, 30, 20, 5]


# Sunset/Sunrise RGB & White LED Colour values over time
#             Time (Seconds)    R,  G,  B,  W
sunrise_colour_map = {  3600: night_colour,
                        3000: [  0,  50, 100,  15],  #Dim Blue
                        2400: [100,  30,  30,  30],  #Neutral
                        1800: [255,   0,   0, 60],  #Very Red
                        1500: [255, 100,   0, 80],  #Sepia dimmer
                        1200: [255, 200,   0, 100],  #Sepia Light
                         900: [ 75, 255,   0, 100],  #Warmer Daylight
                           0: day_colour }     # Bright white


sunset_colour_map = {   3600: day_colour,
                        3000: [ 75, 255,   0, 100],  #Warmer Daylight
                        2400: [255, 200,   0, 100],  #Sepia Light
                        1800: [255, 100,   0,  80],  #Sepia dimmer
                        1500: [255,   0,   0,  60],  #Very Red
                        1200: [100,  30,  30,  30],  #Neutral
                         900: [  0,  50, 100,  15],  #Dim Blue
                           0: night_colour }




# SQL Database (Optional)
ENABLE_DB = False
db_dialect_driver = 'mysql' # See http://docs.sqlalchemy.org/en/latest/core/engines.html
db_name = 'terrarium'
db_user = 'root'
db_pass = 'somesecurepassword'
db_address = '127.0.0.1'