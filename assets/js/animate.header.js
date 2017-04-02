$(document).ready(function(){

  $('#logo-r, #logo-g, #logo-b').jrumble({
  	x: 2,
  	y: 2,
  	rotation: 1,
  	opacity: true,
	opacityMin: .75,
	speed: 100
  });

  $('#logo-r, #logo-g, #logo-b').trigger('startRumble');
});