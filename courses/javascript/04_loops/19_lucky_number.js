// Assign a lucky number
let luckyNumber  = 7;
// Assign randomized generated number to `guess`
let guess = Math.floor(Math.random() * 10) + 1;
// Loop if guess is not equal to `luckyNumber`
while (guess != luckyNumber) {
  // If not equal
  console.log("Nope, it isn't", guess);
  // For each loop regenerate a new random number to `guess` so the while loop continues
  guess = Math.floor(Math.random() * 10) + 1;
}
//  If NOT equal to luckyNumber
console.log("My lucky number is", luckyNumber + "!");
