function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function createBalloon() {
    var balloon = document.createElement('div');
    balloon.className = 'balloon';

    // Set random initial position
    var initialX = getRandomInt(0, window.innerWidth - 50); // 50 is the balloon width
    var initialY = getRandomInt(0, window.innerHeight - 70); // 70 is the balloon height
    balloon.style.left = initialX + 'px';
    balloon.style.top = initialY + 'px';

    balloon.onclick = function() { popBalloon(balloon); };
    
    // Append the balloon to the game container
    document.getElementById('game-container').appendChild(balloon);
    
    // Set random animation duration
    var animationDuration = getRandomInt(3, 8); // Random duration between 3 and 8 seconds
    balloon.style.animation = 'floatUp ' + animationDuration + 's linear';
}

function popBalloon(balloon) {
    balloon.style.animation = 'pop 0.3s ease-out';
    setTimeout(function () {
        balloon.remove();
    }, 300);
}

// Create balloons on page load
document.addEventListener('DOMContentLoaded', function() {
    for (var i = 0; i < 25; i++) {
        createBalloon();
    }
});
