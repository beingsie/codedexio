// 3 animals as objects

let pig = {
  name: "Peppa Pig",
  type: "pig",
  age: 18,
  // Method
  makeSound () {
    console.log("Oink! Oink!");
  },
};

let sheep = {
  name: "Sheepy",
  type: "Sheep",
  age: 19,
  // Method
  makeSound () {
    console.log("Baah! Baah!");
  },
};

let dog = {
  name: "Shilo",
  type: "Dog",
  age: 20,
  // Method
  makeSound () {
    console.log("Woof! Woof!");
  },
};

// Run methods (functions within the objects)
pig.makeSound();
sheep.makeSound();
dog.makeSound();
