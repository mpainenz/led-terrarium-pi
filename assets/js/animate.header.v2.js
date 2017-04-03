$(document).ready(function() {
    randomAnimation($('#logo-r'));
});


function randomAnimation(target) {
    x = (Math.random() * 4) - 2;
    y = (Math.random() * 4) - 2;
    
    target.animate({
        top: y,
        left: x
    }, 100, "swing", function() {
        randomAnimation(target);
    });

};
