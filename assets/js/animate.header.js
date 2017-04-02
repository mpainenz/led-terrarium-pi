$(document).ready(function(){

  $('#logo-r').jrumble({
  	x: 2,
  	y: 1,
  	rotation: 0,
  	opacity: true,
	opacityMin: .2,
	speed: 270
  });

  $('#logo-g').jrumble({
    x: 1,
    y: 2,
    rotation: 0,
    opacity: true,
  	opacityMin: .2,
  	speed: 260
  });

  $('#logo-b').jrumble({
    x: 1,
    y: 2,
    rotation: 0,
    opacity: true,
  	opacityMin: .2,
  	speed: 250
  });

  $('#logo-w').jrumble({
    x: 0,
    y: 0,
    rotation: 0,
    opacity: true,
  	opacityMin: .9,
  	speed: 50
  });

  $('#logo-r, #logo-g, #logo-b, #logo-w').trigger('startRumble');
});