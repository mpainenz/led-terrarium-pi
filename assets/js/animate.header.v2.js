$(document).ready(function() {
    randomMovement($('#logo-r'));
    randomMovement($('#logo-g'));
    randomMovement($('#logo-b'));
    //randomOpacity($('#logo-glow'));
});


function randomMovement(target) {
    x = (Math.random() * 6) - 3;
    y = (Math.random() * 6) - 3;
    speed = Math.floor(Math.random() * 300) + 300; 
    
    target.velocity({
        top: y,
        left: x
    }, speed, "swing", function() {
        returnMovement(target);
    });
};

function returnMovement(target) {
    target.velocity({
        top: 0,
        left: 0
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
