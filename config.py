import Adafruit_DHT

# Set to true to run through Sunrise colours in Demo mode
DEMO_MODE = False # Fast forward mode
DEMO_SPEED = 100 #1 sec = x sec

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
day_colour = (0, 75, 0, 25)

# RGBW Value to use during Night
night_colour = (0, 20, 20, 0)


# Sunset/Sunrise RGB & White LED Colour values over time
#             Time (Seconds)    R,  G,  B,  W
sunrise_colour_map = {  3600: night_colour,
                        3000: (  0, 20,100,  3),   #Blue
                        2400: ( 20, 40, 20,  3),
                        1800: ( 40, 40, 10,  0),   # Sun begins to rise
                        1500: ( 80, 30,  5,  5),
                        1200: ( 90, 60,  0, 10),   # Yellowish
                         900: ( 60, 75,  0, 15),   # White
                           0: day_colour }     # Bright white



# SQL Database (Optional)
enable_db = True
db_dialect_driver = 'mysql' # See http://docs.sqlalchemy.org/en/latest/core/engines.html
db_name = 'terrarium'
db_user = 'root'
db_pass = 'somesecurepassword'
db_address = '127.0.0.1'