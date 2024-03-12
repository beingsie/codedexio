// // Pizza 1

// const pizzaTopping = "Cheese 🧀";
// const pizzaType = "Pan";
// const pizzaSlices = 8;
// const pizzaPrice = 12.99;

// // Pizza 2

// const pizza = {
//   topping: "Pepperoni 🍕",
//   type: "Hand-tossed",
//   slices: 12,
//   price: 14.99,
// };

// console.log(pizza);

// Define a Player class with a method
function Player(name, position, number, nationality) {
  this.name = name;
  this.position = position;
  this.number = number;
  this.nationality = nationality;

  this.introduce = function () {
    return `Hi, I'm ${this.name}, I play as a ${this.position} for Manchester City.`;
  };
}

// Create a new player object using the Player class
let player1 = new Player("Kevin De Bruyne", "Midfielder", 17, "Belgian");

// Call the introduce method
console.log(player1.introduce()); // Output: Hi, I'm Kevin De Bruyne, I play as a Midfielder for Manchester City.
