// Create greetings function
function greetings() {
  // Generate a random number
  const randomNumber = Math.floor(Math.random() * 4) + 1;
  // Determine which greeting is displayed based on the randomly generated number
  if (randomNumber == 1){
    // Log to console
    console.log("Howdy!");
  } else if (randomNumber == 2) {
    // Log to console
    console.log("Hi there!");
  } else if (randomNumber == 3) {
    // Log to console
    console.log("Hey what's happening?");
  } else if (randomNumber == 4) {
    // Log to console
    console.log("Hola!");
  } else {
    // Log to console
    console.log("Heya!");
  }
}
// Run grettings functions 3 times
greetings();
greetings();
greetings();
