// Modified version of the greeting function on Codedex

// Array containing all MCFC players
const mcfcPlayers = [
  "Erling Haaland",
  "Kevin De Bruyne",
  "Jérémy Doku",
  "Phil Foden",
  "Julián Álvarez",
  "Rodri",
  "Matheus Nunes",
  "Jack Grealish",
  "Oscar Bobb",
  "Micah Hamilton",
  "Bernardo Silva",
  "Ederson",
  "Joško Gvardiol",
  "Rico Lewis",
  "Kyle Walker",
  "Mateo Kovačić",
  "Rúben Dias",
  "Nathan Aké",
  "Manuel Akanji",
  "John Stones",
  "Stefan Ortega",
  "Mahamadou Susoho",
  "Sergio Gómez",
]
// Number of players required to qualify
const playersRequired = 11;
// Initialize random number
let randomNumber;
// Function to generate random number
function randomNumberGenerator() {
  randomNumber = Math.floor(Math.random() * mcfcPlayers.length);
}
// Initialize selected lineup
let selectedLineup = [];

for (i = 0; i < playersRequired; i++) {
  randomNumberGenerator();
  // Check duplicate
  if (randomNumber === mcfcPlayers[i]) {
    console.log("Duplicate detected!");
  } else {
    selectedLineup.push(mcfcPlayers[randomNumber]);
  }
}

console.log(selectedLineup);
