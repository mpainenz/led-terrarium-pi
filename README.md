# led-terrarium-pi
Raspberry Pi Controlled LED Terrarium

Uses a Sensor (DHT11, DHT22 or AM2302) to measure heat and humidity


Set the Timezone on your Raspberry Pi with 'sudo raspi-config' command. Defaults to UTC

Requirements:
Python 2.7
pigpio (GPIO lib for accurate and functional GPIO access)
ephem (Astrological lib to work out Sunrise/Sunset. Requires python-dev (sudo apt-get python-dev))
Adafruit Python DHT (Lib for connection to Temp/Humidity Sensor) (https://github.com/adafruit/Adafruit_Python_DHT)
pygal (Graphing Library)

Optional when storing to Database:
SQLAlchemy
MYSQL (Or other SQL Alchemy supported DB)
