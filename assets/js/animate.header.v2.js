$(document).ready(function() {
    randomAnimation();
});


function randomAnimation() {
    x = (Math.random() * 4) - 2
    y = (Math.random() * 4) - 2
    
    $('#logo-r').animate({
        top: y,
        left: x
    }, 100, "swing" function() {
        randomAnimation();
    });

};
