# led-terrarium-pi
Raspberry Pi Controlled LED Terrarium

Uses a Sensor (DHT11, DHT22 or AM2302) to measure heat and humidity


Set the Timezone on your Raspberry Pi with 'sudo raspi-config' command. Defaults to UTC

Requirements:
* Python 2.7
* pigpio (GPIO lib for accurate and functional GPIO access)
* python-dev - `sudo apt-get install python-dev`
* build-essential - `sudo apt-get install build-essential`
* ephem (Astrological lib to work out Sunrise/Sunset) - `sudo pip install emphem`
* Adafruit Python DHT (Lib for connection to Temp/Humidity Sensor) (https://github.com/adafruit/Adafruit_Python_DHT)
* pygal (Graphing Library) - `sudo pip install pygal`

Optional when storing to Database:
SQLAlchemy
MYSQL (Or other SQL Alchemy supported DB)
