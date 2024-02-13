// Modified version of the greeting function on Codedex

// Function generates a random MCFC team lineup 
function mcfcLineup() {
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
  // Number of players for a full team
  const requiredPlayers = 11;
  // Initialize selectedLineup array
  const selectedLineup = [];

  for (i = 1; i < requiredPlayers + 1; i++) {
    // Generated a random number
    const randomNumber = Math.floor(Math.random() * requiredPlayers) + 1;
    // Initialize random selected player
    let mcfcPlayer;
    // Iterate through mcfcPlayers array
    for (x = 0; x < mcfcPlayers.length + 1; x++) {
      mcfcPlayer = mcfcPlayers[x];
    }
    // Check for duplicates
    if (randomNumber == mcfcPlayer)
    // Add players to selected lineup using the random number as the index
    selectedLineup.push(mcfcPlayers[randomNumber]);
  }

  // Print updated selectedLineup array
  console.log(selectedLineup);
}

mcfcLineup();
