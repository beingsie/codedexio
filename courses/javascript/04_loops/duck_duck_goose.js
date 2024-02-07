// Generate a randomized number from 0-9
let randomNumber = Math.floor(Math.random() * 10);
// While loop if randomNumber not 7
while (randomNumber != 7) {
  // Print to console
  console.log("Duck 🦆");
  // Regenerate to stay within loop
  randomNumber = Math.floor(Math.random() * 10);
}
// Print to console
console.log("Goose! 🦢");
