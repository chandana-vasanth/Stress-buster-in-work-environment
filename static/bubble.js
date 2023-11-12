document.addEventListener("DOMContentLoaded", function () {
    const bubbleContainer = document.getElementById("bubble-container");

    // Create bubbles dynamically
    for (let i = 0; i < 25; i++) {
        const bubble = document.createElement("div");
        bubble.classList.add("bubble");
        bubble.addEventListener("click", popBubble);
        bubbleContainer.appendChild(bubble);
    }

    function popBubble(event) {
        const bubble = event.target;
        bubble.style.opacity = 0;
        playPopSound();
    }

    function playPopSound() {
        const popSound = new Audio("/static/relax.mp3"); // Adjust the path based on your sound file location
        popSound.play();
    }
});
