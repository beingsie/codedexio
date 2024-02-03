// Initialize player choice
let player = 2;
let playerName = 'Player';

// Generate a random number between 0-3 for the bot's choice
let bot = Math.floor(Math.random() * 3 + 1);
let botName = 'Bot';

// Rock, Paper or Scissors
let rock = 0;
let paper = 1;
let scissors = 2;

// Compare values
if (player == bot) {
  console.log('It\'s a draw!')
} else if (player == rock && bot == scissors) {
  console.log('Rock beats Scissors')
} else if (player == scissors && bot == paper) {
  console.log('Scissors beats Paper')
} else if (player == paper && bot == rock) {
  console.log('Paper beats Rock')
} else {
  console.log('Error, please try again.')
}

// Won't Bot always lose? Does this favor the player?
