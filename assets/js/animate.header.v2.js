$(document).ready(function() {
    randomMovement($('#logo-r'));
    randomMovement($('#logo-g'));
    randomMovement($('#logo-b'));
    randomOpacity($('#logo-glow'));
});


function randomMovement(target) {
    x = (Math.random() * 6) - 3;
    y = (Math.random() * 6) - 3;
    
    target.velocity({
        top: y,
        left: x
    }, 1000, "swing", function() {
        randomMovement(target);
    });
};

function randomOpacity(target) {
    o = (Math.random() * .5) + .5;
    
    target.velocity({
        opacity: o
    }, 1000, "swing", function() {
        randomOpacity(target);
    });
};
