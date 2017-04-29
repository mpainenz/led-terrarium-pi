# LED Terrarium Build Guide

## How to build your own Raspberry Pi powered Terrarium


<div class="parallax-window"
     id="image1"
     data-parallax="scroll" 
     data-image-src="/led-terrarium-pi/assets/img/test.jpg">         
</div>

<div class="main-content">

<h1 id="led-terrarium-pi">led-terrarium-pi</h1>
<p>Raspberry Pi Controlled LED Terrarium</p>

<p>Uses a Sensor (DHT11, DHT22 or AM2302) to measure heat and humidity</p>

<p>Set the Timezone on your Raspberry Pi with ‘sudo raspi-config’ command. Defaults to UTC</p>

<p>Requirements:</p>
<ul>
  <li>Python 2.7 (Installed by default)</li>
  <li>pigpio (GPIO lib for accurate and functional GPIO access)</li>
</ul>

<p>Packages</p>
<ul>
  <li>python-dev - <code class="highlighter-rouge">sudo apt-get install python-dev</code></li>
  <li>build-essential - <code class="highlighter-rouge">sudo apt-get install build-essential</code></li>
  <li>mysql-server - <code class="highlighter-rouge">sudo apt-get install mysql-server</code></li>
  <li>libmysqlclient-dev - <code class="highlighter-rouge">sudo apt-get install libmysqlclient-dev</code></li>
</ul>

<p>Python Libraries</p>
<ul>
  <li>Adafruit Python DHT (Lib for connection to Temp/Humidity Sensor) (https://github.com/adafruit/Adafruit_Python_DHT)</li>
  <li>ephem (Astrological lib to work out Sunrise/Sunset) - <code class="highlighter-rouge">sudo pip install emphem</code></li>
  <li>pygal (Graphing Library) - <code class="highlighter-rouge">sudo pip install pygal</code></li>
  <li>sqlalchemy - <code class="highlighter-rouge">sudo pip install sqlalchemy</code></li>
  <li>MySQL-python - <code class="highlighter-rouge">sudo pip install MySQL-python</code></li>
</ul>

</div>
