$(document).ready(function(){

  $('#logo-r').jrumble({
  	x: 2,
  	y: 1,
  	rotation: 0,
  	opacity: true,
	opacityMin: .2,
	speed: 50
  });

  $('#logo-g').jrumble({
    x: 1,
    y: 2,
    rotation: 0,
    opacity: true,
  	opacityMin: .2,
  	speed: 75
  });

    $('#logo-b').jrumble({
    x: 1,
    y: 2,
    rotation: 0,
    opacity: true,
  	opacityMin: .2,
  	speed: 75
  });

  $('#logo-r, #logo-g, #logo-b').trigger('startRumble');
});