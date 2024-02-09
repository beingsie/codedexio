// Array of favorite songs (playlist)
const musicPlaylist = [
  "Tom Sawyer",
  "Sabotage",
  "I Wanna Dance With Somebody",
  "Don't Speak",
  "Bulls On Parade",
  "Thriller",
  "The Breaks",
  "Brick",
  "Aeroplane Over the Sea",
  "Tubthumping"
];

// Remove first element of the array
musicPlaylist.shift();
// Remove the last element of the array
musicPlaylist.pop();
// Add a new element to the end of the array
musicPlaylist.unshift("Homeless Door");
// Add a new element to the beginning of the array
musicPlaylist.push("So");

// Display updated playlist
console.log(musicPlaylist);
