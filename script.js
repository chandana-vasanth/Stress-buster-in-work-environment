const container = document.querySelector(".container");
const circleText = document.querySelector(".circleText");
const totalTime = 7500;
const breathTime = (totalTime / 5) * 2;
const holdTime = totalTime / 5;

breathAnimation();

function breathAnimation() {
  circleText.innerHTML = "breath in";
  container.className = "container grow";
  setTimeout(() => {
    circleText.innerHTML = "hold";
    setTimeout(() => {
      circleText.innerHTML = "breath out";
      container.className = "container shrink";
    }, holdTime);
  }, breathTime);
}

setInterval(breathAnimation, totalTime);
