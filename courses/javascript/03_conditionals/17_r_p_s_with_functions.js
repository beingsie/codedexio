// Player choice
let playerChoice = 2;
let playerName = "Player";

// Generate a random number between 0-3 for the bot's choice
let botChoice = Math.floor(Math.random() * 3 + 1);
let botName = "Bot";

// Rock, Paper or Scissors
let rock = 0;
let paper = 1;
let scissors = 2;

function draw() {
  console.log("Ran draw() successfully"); //DEBUG

  // Draw message
  function consoleMessageDraw() {
    console.log("It's a draw!");
  }

  // Check if its a draw
  if (playerChoice === botChoice) {
    consoleMessageDraw();
  } else {
    // Otherwise check winner & display results
    winner();
  }
}

function winner() {
  console.log("Ran winner() successfully"); //DEBUG

  // Initialization for winning player/hand
  let winningPlayer;
  let winningHand;

  function choiceMessage() {
    console.log("Ran choiceMessage() successfully"); //DEBUG

    // Display each player's choice
    console.log(playerName, "picked:", playerChoice);
    console.log(botName, "picked:", botChoice);
  }

  // Determine winning hand & winning player
  if (playerChoice === rock) {
    // If user plays rock
    winningHand = rock;
    winningPlayer = playerName;
  } else if (botChoice === rock) {
    // If bot plays rock
    winningHand = rock;
    winningPlayer = botName;
  } else if (playerChoice === scissors) {
    // If user plays scissors
    winningHand = scissors;
    winningPlayer = playerName;
  } else if (botChoice === scissors) {
    // If bot plays scissors
    winningHand = scissors;
    winningPlayer = botName;
  } else if (playerChoice === paper) {
    // If user plays paper
    winningHand = paper;
    winningPlayer = playerName;
  } else if (botChoice === paper) {
    // If bot plays paper
    winningHand = paper;
    winningPlayer = botName;
  }

  // Winning message
  function winningHandMessage() {
    console.log("winningHandMessage() successfully"); //DEBUG

    // Winning hand messages
    let rockVsScissors = "Rock crushes Scissors!";
    let scissorsVsPaper = "Scissors defeat Paper!";
    let paperVsRock = "Paper defeats Rock!";

    // Display message by winning hand
    if (winningHand === rock) {
      console.log(rockVsScissors);
    } else if (winningHand === scissors) {
      console.log(scissorsVsPaper);
    } else {
      console.log(paperVsRock);
    }
  }

  function displayWinner() {
    console.log("displayWinner() successfully"); //DEBUG

    // Display winning player
    console.log("The", winningPlayer, "won!");
  }

  // All winning messages as victory result
  function victory() {
    winningHandMessage();
    choiceMessage();
    displayWinner();
  }

  // Run victory message
  victory();
}

// Run the draw (Initial process)
draw();
