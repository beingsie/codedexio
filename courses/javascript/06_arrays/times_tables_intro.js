// Array of Manchester City FC players
let manchesterCityPlayers = [
	"Ederson",
	"Erling Haaland",
	"Jack Grielish",
	"Jeremy Doku",
	"Phil Phoden",
];

// Get array length
let totalManchesterCityPlayers = manchesterCityPlayers.length;
// Display length interger as total Manchester City players
console.log("There are currently", totalManchesterCityPlayers, "players in Manchester City FC");

// Array of player position numbers
const playerNumbers = [9, 10, 11, 47];

// Iterate through array & print out player numbers
for (let i = 0; i < totalManchesterCityPlayers - 1; i++) {
  console.log(playerNumbers[i]);
}

// Initialize counter (starting from 0)
let counter = 0;
// Loop through Manchester City players via length
while (counter < manchesterCityPlayers.length) {
  // Print every indice in the array
  console.log(manchesterCityPlayers[counter]);
  // Increase counter by one every time a loop completes
  counter++;
}
