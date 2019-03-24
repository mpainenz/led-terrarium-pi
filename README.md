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

<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/gpio.jpg?sanitize=true&raw=true">

<p>GPIO pins either accept an input voltage which can be read, or can be setup to output a voltage signal. In this case, we want to power our LED lights, so we want to output a signal. In our software, we tell the Raspberry Pi that we want to use three pins to control the RGB light strip (one for each colour), and one pin to control the White LED strip.</p>

<p>Sounds simple right? Unfortunately there are two problems...</p>

<ul>
  <li>The LED strips require 12 volts, but the GPIO pins only output 3.3 volts. </li>
  <li>The output voltage on the GPIO pins can either be 3.3v or 0v. There's no in-between. For an RGB light strip to show a full range of colours, or a white strip to be at varying brightnesses, we need the values in between the min and max voltage</li>
</ul>

<p>Fortunately, we have solutions to both of these issues. </p>


<h2 id="led-terrarium-pi">MOSFET</h2>

<p>Instead of using the Raspberry Pi GPIO pins to power the LED strips (which wouldn't work because the output voltage is too low at 3.3v when we need 12v), we will instead power the LED strips off a 12v power supply, and introduce a MOSFET into that circuit.</p>
  
<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/12901-01.jpg?sanitize=true&raw=true">

<p>Think of the MOSFET here as a type of switch. The MOSFET has two circuits running through it. When current passes through one of those circuits, it opens the other circuit. </p>

<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/diagram1_bb.png?sanitize=true&raw=true">

<p>We connect our Raspberry Pi and our LED light strip to our MOSFET. I've shown one MOSFET here, but we would need to add one per colour on the RGB strip, and another one for our White LED strip. Each of these are controlled separately to achieve a full colour spectrum</p>


<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/mosfet.png?sanitize=true&raw=true">
  
<p>A MOSFET has three pins. From left to right, Gate, Drain, Source.</p>

<p>The Gate pin is what is connected to the Raspberry Pi, and is used to open the Source/Drain circuit. You might notice that we need to also connect the Gate pin to negative with a resistor. When voltage is applied to the Gate pin, it charges up like a capacitor, so it must also be attached to negative with a resistor. If you skip that step, the gate will remain open when voltage is not being applied. The resistor allows the Gate to discharge.</p>


<p>The LED circuit is attached to the Source Pin, and then the Drain is connected to the negative terminal of the power source. Unless voltage is being applied to the Gate, this circuit remains closed.</p>

<p>The part I have used here (Part Number IRLZ34N) is a perfect fit for a 12v LED light circuit. It is rated to work with the Raspberry Pi's 3.3v output and the 12v light circuit. There are two types of MOSFETS, and they are wired differently. This is an N-type MOSFET.</p>

  



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

