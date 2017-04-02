$(document).ready(function(){

  $('#logo-r, #logo-g, #logo-b').jrumble({
  	x: 2,
  	y: 2,
  	rotation: 0.5,
  	opacity: true,
	opacityMin: .5,
	speed: 150
  });

  $('#logo-r, #logo-g, #logo-b').trigger('startRumble');
});