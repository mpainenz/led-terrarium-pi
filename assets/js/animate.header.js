$(document).ready(function(){

  $('#logo-r').jrumble({
  	x: 1,
  	y: 1,
  	rotation: 0,
  	opacity: true,
	opacityMin: .2,
	speed: 170
  });

  $('#logo-g').jrumble({
    x: 1,
    y: 1,
    rotation: 0,
    opacity: true,
  	opacityMin: .2,
  	speed: 180
  });

  $('#logo-b').jrumble({
    x: 1,
    y: 1,
    rotation: 0,
    opacity: true,
  	opacityMin: .2,
  	speed: 190
  });

  $('#logo-w').jrumble({
    x: 0,
    y: 0,
    rotation: 0,
    opacity: true,
  	opacityMin: .8,
  	speed: 30
  });

  $('#logo-r, #logo-g, #logo-b, #logo-w').trigger('startRumble');
});
