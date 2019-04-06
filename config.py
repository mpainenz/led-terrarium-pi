#import Adafruit_DHT

# GPIO Channel for RGB LED Strip
r_channel = 25
g_channel = 27
b_channel = 22

# GPIO Channel for white LED Strip
w_channel = 18

# Location Latitude and Longitude (Auckland, New Zealand)
latitude = "-36.84"
longitude = "174.74"


# RGBW Value to use during Day
day_colour = [75, 255, 0, 100]

# RGBW Value to use during Night
#night_colour = [0, 200, 200, 0]
night_colour = [0, 100, 100, 0]


# Sunset/Sunrise RGB & White LED Colour values over time
#             Time (Seconds)    R,  G,  B,  W

# 60 = 1 Minute
# 3600 = 1 hour
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




# Set to true to run through Sunrise colours in Demo mode
DEMO_MODE = False # Fast forward mode
DEMO_SPEED = 10 #1 sec = x sec
