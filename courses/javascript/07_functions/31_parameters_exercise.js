// Top players & their current total goals scored
let topPlayers = [
  { name: 'Haaland', goals: 16 },
  { name: 'Mbappe', goals: 20 },
  { name: 'Kane', goals: 24 },
  { name: 'Ronaldo', goals: 20 },
  { name: 'Estrada', goals: 66 },
]

function favPlayerGoals(mostGoals) {
  // Iterate through the array
  for (i = 0; i < topPlayers.length; i++) {
    // Determine if the players have scored more than 20 goals
    if (topPlayers[i].goals > 20) {
      // If condition is true display top scorer message
      console.log(`${topPlayers[i].name} is currently the top scorer in football.`);
    }
  }
}
// Print message by running function
console.log(favPlayerGoals());
