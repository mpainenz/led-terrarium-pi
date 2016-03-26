# led-terrarium-pi
Raspberry Pi Controlled LED Terrarium

Uses a Sensor (DHT11, DHT22 or AM2302) to measure heat and humidity


Set the Timezone on your Raspberry Pi with 'sudo raspi-config' command. Defaults to UTC

Requirements:
Python 2.7
pigpio
ephem (requires python-dev (sudo apt-get python-dev))
Adafruit Python DHT (https://github.com/adafruit/Adafruit_Python_DHT)

Optional when storing to Database:
SQLAlchemy
MYSQL (Or other SQL Alchemy supported DB)
