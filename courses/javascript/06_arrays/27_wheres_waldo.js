// Assign Waldo as a string value (to avoid repitition)
let waldo = "Waldo";
// Array of characters
const characters = [
  "The Wally Watchers",
  "Wilma",
  "Fritz",
  "Wizard Whitebeard",
  "Odlaw",
  waldo, // Insert string variable
  "Woof"
];
// Check if characters array contains waldo value
if ((characters).includes(waldo)) {
  // Assign the index of waldo in characters array to a variable
  let waldoIndex = characters.indexOf(waldo);
  //  Print found message
  console.log("Found", waldo, "at index", waldoIndex + "!");
} else {
  // Otherwise display not found message
  console.log(waldo, "was not found.");
}
