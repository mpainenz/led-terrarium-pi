<div class="main-content">
  <h2 id="how-to-build-your-own-raspberry-pi-powered-terrarium">Build your own Raspberry Pi powered Terrarium</h2>
  <p>Use a Raspberry Pi to control LED lighting for a terrarium. 
    Download the code I've shared on <a href="https://github.com/mpainenz/led-terrarium-pi">my Github page</a>, and build your own!
  </p>
  <ul>  
    <li>Changes colour throughout the sunrise, day, sunset, and night</li>  
    <li>Uses your geographical location to calculate the actual sunrise and sunset times to use</li>
  </ul>
  
  
  <h2 id="you-will-need">You will need...</h2>
  <ul>
    <li>A Raspberry Pi (any version will do)</li>
    <li>A Terrarium</li>
    <li>A White LED Light strip (to provide light to the plants)</li>
    <li>An RGB LED Light strip (to provide color effects)</li>
    <li>A 12v DC Power Supply</li>   
    <li>A 12v to 5v UBEC (Powers your Pi from the same 12v supply as the LED strips)</li>
    <li>A soldering iron and solder</li>
    <li>4 x MOSFET Transistors (Used in the lighting circuits)</li>
    <li>4 x Resistors (Also used in the lighting circuits)</li>
    <li>Various lengths of electrical wire</li>
  </ul>

<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/20160201_110606.jpg?sanitize=true&raw=true">
<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/DSC00015.JPG?sanitize=true&raw=true">

<h2 id="lets-get-started">Lets get started</h2>

<p>It might seem complicated, but it's pretty straight forward once we break it down into parts. Keep scrolling and we can go through each step. If you get stuck, feel free to send me an email. Perhaps I could make one for you?</p>
  
<p>Keep scrolling for more...</p>


</div>

<div class="parallax-window"
     id="image1"
     data-parallax="scroll" 
     data-image-src="/led-terrarium-pi/assets/img/test.jpg">         
</div>

<div class="main-content">


<h2 id="led-terrarium-pi">Powering the lights</h2>
<p>How can a Raspberry Pi control LED lighting?</p>

<p>All Raspberry Pi's come with a series of GPIO pins which you can control.</p>

<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/DSC00015.JPG?sanitize=true&raw=true">

<p>GPIIO pins either accept an input voltage which can be read, or output a signal. In this case, we want to power our LED lights, so we want to output a signal.</p>


<h2 id="led-terrarium-pi">Installing the software</h2>

<p>Firstly prepare a Rasperry Pi by installing Raspian OS, and set the Timezone on your Raspberry Pi with ‘sudo raspi-config’ command. (Defaults to UTC)</p>

<p>Requirements:</p>
<ul>
  <li>Python 2.7 (usually installed for you)</li>
  <li>pigpio (Also usually installed)</li>
</ul>

<p>Python Libraries</p>
<ul>
  <li>ephem (Astrological lib to work out Sunrise/Sunset) - <code class="highlighter-rouge">sudo pip install emphem</code></li>
</ul>

