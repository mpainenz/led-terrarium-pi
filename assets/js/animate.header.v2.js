$(document).ready(function() {
    randomAnimation($('#logo-r'));
    randomAnimation($('#logo-g'));
    randomAnimation($('#logo-b'));
});


function randomAnimation(target) {
    x = (Math.random() * 6) - 3;
    y = (Math.random() * 6) - 3;
    
    target.animate({
        top: y,
        left: x
    }, 1000, "swing", function() {
        randomAnimation(target);
    });

};
