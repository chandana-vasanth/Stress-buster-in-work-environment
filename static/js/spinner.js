// static/js/spinner.js

const canvas = document.getElementById('spinnerCanvas');
const ctx = canvas.getContext('2d');

const spinnerImage = new Image();

// Use an event listener to ensure the image is loaded before drawing
spinnerImage.addEventListener('load', function() {
    console.log('Image loaded successfully');
    drawSpinner(0);  // Assuming an initial angle of 0
});

spinnerImage.src = "{{ url_for('static', filename='js/spinner.png') }}";  // Adjust the path based on your folder structure

function drawSpinner(angle) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;

    ctx.save();
    ctx.translate(centerX, centerY);
    ctx.rotate(angle);
    ctx.drawImage(spinnerImage, -spinnerImage.width / 2, -spinnerImage.height / 2);
    ctx.restore();
}

function updateSpinner(event) {
    const mouseX = event.clientX - canvas.getBoundingClientRect().left;
    const mouseY = event.clientY - canvas.getBoundingClientRect().top;

    const angle = Math.atan2(mouseY - canvas.height / 2, mouseX - canvas.width / 2);
    drawSpinner(angle);
}

canvas.addEventListener('mousemove', updateSpinner);
