# test heading

## test sub heading

### test sub sub heading


<!--
<div class="parallax-window" 
     data-parallax="scroll" 
     data-image-src="/led-terrarium-pi/assets/img/test.jpg">         
-->


# led-terrarium-pi
Raspberry Pi Controlled LED Terrarium

Uses a Sensor (DHT11, DHT22 or AM2302) to measure heat and humidity


Set the Timezone on your Raspberry Pi with 'sudo raspi-config' command. Defaults to UTC

Requirements:
* Python 2.7 (Installed by default)
* pigpio (GPIO lib for accurate and functional GPIO access)
 
Packages
* python-dev - `sudo apt-get install python-dev`
* build-essential - `sudo apt-get install build-essential`
* mysql-server - `sudo apt-get install mysql-server`
* libmysqlclient-dev - `sudo apt-get install libmysqlclient-dev`

Python Libraries
* Adafruit Python DHT (Lib for connection to Temp/Humidity Sensor) (https://github.com/adafruit/Adafruit_Python_DHT)
* ephem (Astrological lib to work out Sunrise/Sunset) - `sudo pip install emphem`
* pygal (Graphing Library) - `sudo pip install pygal`
* sqlalchemy - `sudo pip install sqlalchemy`
* MySQL-python - `sudo pip install MySQL-python`
