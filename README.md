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

<p align="center">
<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/diagram1_bb.png?sanitize=true&raw=true">
</p>

<p>We connect our Raspberry Pi and our LED light strip to our MOSFET. I've shown one MOSFET here, but we would need to add one per colour on the RGB strip, and another one for our White LED strip. Each of these are controlled separately to achieve a full colour spectrum</p>

<p align="center">
<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/mosfet.jpg?sanitize=true&raw=true">
</p>
  
<p>A MOSFET has three pins. From left to right, Gate, Drain, Source.</p>
<ul>
  <li>The Gate pin is what is connected to the Raspberry Pi, and is used to open the Source/Drain circuit. You might notice that we need to also connect the Gate pin to negative with a resistor. When voltage is applied to the Gate pin, it charges up like a capacitor, so it must also be attached to negative with a resistor. If you skip that step, the gate will remain open when voltage is not being applied. The resistor allows the Gate to discharge.</li>
  
  <li>The Source and Drain pins are attached to the LED circuit. Unless voltage is being applied to the Gate, this circuit remains closed.</li>
</ul>

<p>The part I have used here (Part Number IRLZ34N) is a perfect fit for a 12v LED light circuit. It is rated to work with the Raspberry Pi's 3.3v output and the 12v light circuit. There are two types of MOSFETS, and they are wired differently. This is an N-type MOSFET.</p>

<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/20160131_165812.jpg?sanitize=true&raw=true">

<p>It can be helpful to use a little PCB board to attach the MOSFETs to. The image above was my first attempt. I ended up redoing this part, and not using a PCB. Instead I just used solder, wire, and heat shrink to save a little space.</p>

<p>You might notice that in the picture above, I'm also using the 12v power source to power the Raspberry Pi. The Raspberry Pi can accept 5v power into the GPIO interface. How do we step down from 12v to 5v? We can use a 12v to 5v UBEC. This accepts a 12v source, and outputs a 5v current. This step is optional, you could just use a normal 5v power supply, but I wanted to only have one cable going into the terrarium</p>

</div>
<div class="parallax-window"
     id="image1"
     data-parallax="scroll" 
     data-image-src="/led-terrarium-pi/assets/img/20160203_145956.jpg">         
</div>
<div class="main-content">


<h2 id="led-terrarium-pi">Controlling the lights</h2>

<p>I mentioned earlier that there is another issue here. Our LED strips are analogue. They accept any current between 0v and 12v. For the RGB light strip, to generate a wide selection of colours, that means we want to use all sorts of voltages.</p>

<p>When the Raspberry Pi is instructed to send an output voltage to our MOSFET, it can only send either 0v or 3.3v. There is no in-between. If we could half the voltage and send 1.65v to the gate of the mosfet, we would expect around 6v of current on the light circuit.</p>

<p>So what can we do?</p>

<h2 id="led-terrarium-pi">Pulse Width Modulation</h2>

<p>Feel free to skip this section if you want, I've handled this in the code so you don't really need to understand this part. But if you are interested, what we can do is quickly alternate the output 3.3v signal on and off many times a second. We can then have the software turn that signal on for longer, or off for longer, depending on what volate we want to try and emulate.</p>

<p align="center">
<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/pwm2.jpg?sanitize=true&raw=true">
</p>
  
</div>
<div class="parallax-window"
     id="image1"
     data-parallax="scroll" 
     data-image-src="/led-terrarium-pi/assets/img/DSC00021.JPG">         
</div>
<div class="main-content">


<h2 id="led-terrarium-pi">The fun part</h2>

<p>Now that the hard part is done, putting the terrarium together can start. For mine, I chose to try and build a closed terrarium and grow mosses, lichens, and other moisture loving plants.</p>

<p>To create a healthy enviroment for the plants, it's useful to create a area in the bottom of the container which contains either spagnum moss, or charcoal. My understanding is that this can help to prevent toxic compounds from lingering in the bottom where the water drains. It will help to prevent the envirment in the soil turning anaerobic, and will be more beneficial to the health of the overall system</p>

<p>For my terrarium, I used...</p>
  
  <ul>
    <li>Wild plants and mosses collected from nature</li>
    <li>Small rocks</li>
    <li>Medium sized rocks</li>
    <li>Cacti and Succulent Potting Mix (Formulated to drain very well)</li>
    <li>Spagnum Moss</li>
    <li>Charcoal</li>
    <li>A Coffee Filter</li>
  </ul>
  
<p align="center">
<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/20160312_164059.jpg?sanitize=true&raw=true">
</p>
  

<p>First I started with large rocks at the bottom</p>

<p align="center">
<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/20160312_164917.jpg?sanitize=true&raw=true">
</p>

<p>Next I placed a piece of Coffee filter paper on top </p>

<p align="center">
<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/20160312_165603.jpg?sanitize=true&raw=true">
</p>

<p>And on top of that, a combination of Spagnum Moss and crushed Charcoal (be sure not to use any charcoal that might have a checmical accelerant added to it to help it burn faster)</p>

<p align="center">
<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/20160312_170434.jpg?sanitize=true&raw=true">
</p>


<p>On top of that some small rocks</p>

<p align="center">
<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/20160312_170912.jpg?sanitize=true&raw=true">
</p>

<p>And on top of that some potting mix</p>

<p align="center">
<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/20160312_171522.jpg?sanitize=true&raw=true">
</p>


<p>Now that we have a functional drainage and bedding layer, the plants can be added. This part was difficult to photograph, but essentially it's a bit of a jigsaw puzzle, and is really an art form in itself. </p>

<p align="center">
<img src="https://github.com/mpainenz/led-terrarium-pi/blob/master/assets/img/20160425_111446.jpg?sanitize=true&raw=true">
</p>


</div>
<div class="parallax-window"
     id="image1"
     data-parallax="scroll" 
     data-image-src="/led-terrarium-pi/assets/img/20160320_183034.jpg">         
</div>
<div class="main-content">




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

