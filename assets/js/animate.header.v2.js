$(document).ready(function() {
    randomMovement($('#logo-r'));
    randomMovement($('#logo-g'));
    randomMovement($('#logo-b'));
    randomOpacity($('#logo-glow'));
});


function randomMovement(target) {
    x = (Math.random() * 4) - 2;
    y = (Math.random() * 4) - 2;
    //speed = Math.floor(Math.random() * 300) + 200; 
    
    target.velocity({
        top: y,
        left: x
    }, 400, "swing", function() {
        returnMovement(target);
    });
};

function returnMovement(target) {
    target.velocity({
        top: 0,
        left: 0
    }, 400, "swing", function() {
        randomMovement(target);
    });
};

function randomOpacity(target) {
    o = (Math.random() * .4) + .6;
    
    target.velocity({
        opacity: o
    }, 500, "swing", function() {
        returnOpacity(target);
    });
};

function returnOpacity(target) {
    target.velocity({
        opacity: 0.4
    }, 500, "swing", function() {
        randomOpacity(target);
    });
};
