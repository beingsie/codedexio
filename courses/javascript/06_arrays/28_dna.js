// DNA array
let dnaPieces = ["A", "C", "G", "T"];
// Initialize empty DNA array to store generated pattern
let myDNA = [];
// Loop 24 times
for (let z = 0; z < 24; z++) {
  // Initialize to contain randomized string pattern
  let dnaString = "";
  // Loop 3 times to create a 3 letter string pattern
  for (let i = 0; i < 3; i++) {
    // Generate a random interger 0-3
    randomIndex = Math.floor(Math.random() * 4);
    // Assign generated string from pieces
    dnaString = dnaString + dnaPieces[randomIndex];
  }
  // Add to main array
  myDNA.push(dnaString);
}
// Print 24-pattern DNA
console.log(myDNA);
