// Initialize a number
let myNum = Math.floor(Math.random() * 10);
// Initialize binary with empty string
let binary = "";

// While method
while (myNum > 0) {
    // Check if divisible by 2
    if (myNum % 2 === 0) {
        binary = "1" + binary;
        // console.log(binary); //DEBUG
    } else {
        binary = "0" + binary;
        // console.log(binary); //DEBUG
    }
    // Reduce myNum by half each time
    myNum = Math.floor(myNum / 2);
}
// Print binary to console
console.log(binary);
