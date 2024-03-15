// Select mood button
const moodBtn = document.getElementById("moodBtn");// Extra 😎

// Function onClick
function changeMood() {// Extra 😎
  // Select mood ring border
  let moodRingBorder = document.getElementById("moodRing");// Extra 😎
  // Toggle spin class (animation)
  moodRingBorder.classList.add("spin");// Extra 😎

  moodRingBorder.addEventListener('animationend', () => {// Extra 😎
    moodRingBorder.classList.remove("spin");
  });

  // Create a variable that selects the element with the id of "stone"
  let stone = document.getElementById("stone");
  // Generate a random number between 1 and 9
  let randomNumber = Math.floor(Math.random() * 10) + 1;

  // Change the .style.backgroundColor property
  // according to the value of randomNumber
  if (randomNumber === 1) {
    stone.style.backgroundColor = "red";
  } else if (randomNumber === 2) {
    stone.style.backgroundColor = "orange";
  } else if (randomNumber === 3) {
    stone.style.backgroundColor = "yellow";
  } else if (randomNumber === 4) {
    stone.style.backgroundColor = "green";
  } else if (randomNumber === 5) {
    stone.style.backgroundColor = "blue";
  } else if (randomNumber === 6) {
    stone.style.backgroundColor = "#4169e1";
  } else if (randomNumber === 7) {
    stone.style.backgroundColor = "#00008b";
  } else if (randomNumber === 8) {
    stone.style.backgroundColor = "purple";
  } else {
    stone.style.backgroundColor = "black";
  }
}
