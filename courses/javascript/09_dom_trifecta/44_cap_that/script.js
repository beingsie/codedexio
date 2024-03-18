// Meme img array
const memeArray = [
  "https://i.imgur.com/bSi4xLb.png",
  "https://i.imgur.com/6y0G7N0.png",
  "https://i.imgur.com/LXnRao1.png",
  "https://i.imgur.com/Qqoxh1N.png"
];

// Meme captions array
let captionsArray = [
  "When you try to 'git commit' on a Friday night...",
  "Why don't we tell secrets in code? Because it's always getting leaked.",
  "JavaScript says to JSON: 'I thought you were an object of mine.'",
  "Just debugging it makes it work...every programmer's nightmare!",
  "No coffee, no codie.",
  "That moment when you realize it's not the semicolon...",
  "It's not a bug, it's an undocumented feature."
];

// Select DOM elements
const randomMeme = document.getElementById("random-meme");
const randomCaption = document.getElementById("random-caption");
const generatorButton = document.getElementById("generator-button");

// Add a "click" event listener to the selected "generator-button"
generatorButton.addEventListener("click", function () {
  // Generate 2 random index numbers between 0 and the length
  // of either the memeArray or the captionArray
  let randomIndexA = Math.floor(Math.random() * memeArray.length);
  let randomIndexB = Math.floor(Math.random() * captionsArray.length);

  // Change the .src property of the selected "random-meme"
  // image element to one of the images in the memeArray
  randomMeme.src = memeArray[randomIndexA];

  // change the .innerText property of the selected "random-caption"
  // heading element to one of the strings in the captionArray
  randomCaption.textContent = captionsArray[randomIndexB]
});
