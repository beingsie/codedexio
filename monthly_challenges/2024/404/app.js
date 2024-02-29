("use strict");

AOS.init({
  duration: 1000, // values from 0 to 3000, with step 50ms
});

let headings = [
  "Yep, URL mites",
  "Pixels were misplaced",
  "Bytes escaped again",
  " A quantum error occured",
];

function selectRandomHeading() {
  let randomInt = Math.floor(Math.random() * headings.length);
  let randomHeading = document.getElementById("randomHeading");
  randomHeading.textContent = headings[randomInt];
}

// JavaScript to spawn "Z" elements in a zigzag pattern and fade them out

document.addEventListener("DOMContentLoaded", function () {
  // Function to spawn "Z" elements
  function spawnZ() {
    const container = document.getElementById("z-container");
    const numZ = 4; // Number of "Z" elements to spawn
    const delay = 200; // Delay between each "Z" spawn in milliseconds

    for (let i = 0; i < numZ; i++) {
      const z = document.createElement("p");
      z.classList.add("press-start", "z-animation");
      z.innerText = "z";
      container.appendChild(z);

      // Apply delay to create zigzag effect
      z.style.animationDelay = `${i * delay}ms`;

      // Fade out animation
      z.style.animationDuration = "1.11s"; // Adjust duration as needed
    }
  }

  selectRandomHeading();
  // Call spawnZ function when the DOM is loaded
  spawnZ();
});

document.addEventListener("DOMContentLoaded", () => {
  const paragraphs = document.querySelectorAll(".terminal p");
  let currentParagraphIndex = 0;
  let i = 0; // Current character index
  let speed = 30; // Typing speed in milliseconds

  function typeWriter() {
    if (currentParagraphIndex < paragraphs.length) {
      const txt = paragraphs[currentParagraphIndex].getAttribute("data-text"); // Store the full text in a data attribute
      if (i < txt.length) {
        paragraphs[currentParagraphIndex].innerHTML += txt.charAt(i);
        i++;
        setTimeout(typeWriter, speed);
      } else {
        // Move to the next paragraph
        currentParagraphIndex++;
        i = 0; // Reset character index for the new paragraph
        setTimeout(typeWriter, 200); // Wait a bit before starting the next paragraph
      }
    }
  }

  // Initialize each paragraph with a data-text attribute and clear its text content
  paragraphs.forEach((p) => {
    const text = p.textContent;
    p.setAttribute("data-text", text);
    p.textContent = ""; // Clear the text content so we can type it out
  });

  typeWriter(); // Start typing
});

const backHomeButton = document.getElementById("backHome");
let mainHeroContent = document.getElementById("mainHeroContent");
let mainHeroContent2 = document.getElementById("mainHeroContent2");
let rocketGif = document.getElementById("rocketGif");

backHomeButton.addEventListener("click", function () {
  mainHeroContent.setAttribute("data-aos", "fade-down");

  setTimeout(function () {
    rocketGif.classList.add("exit-right");
  }, 1200);

  setTimeout(function () {
    window.location.href = "https://www.codedex.io/home";
  }, 4444);
});
