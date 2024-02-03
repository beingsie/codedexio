// Simpler solution suggested by Codedex

// User question
let userQuestion = "Can I learn JavaScript fundamentals in a week?";
// Randomize a number between 0 to 9
let magic8Random = Math.floor(Math.random() * 10);
// Answer
let answer = ""

if (magic8Random == 1) {
    answer = "Yes - definitely.";
} else if (magic8Random == 2) {
    answer = "It is decidedly so.";
} else if (magic8Random == 3) {
    answer = "Without a doubt.";
} else if (magic8Random == 4) {
    answer = "Reply hazy, try again.";
} else if (magic8Random == 5) {
    answer = "Ask again later.";
} else if (magic8Random == 6) {
    answer = "Better not tell you now.";
} else if (magic8Random == 7) {
    answer = "My sources say no.";
} else if (magic8Random == 8) {
    answer = "Outlook not so good.";
} else {
    answer = "Very doubtful.";
}

// Display user question
console.log("Question: ", userQuestion);
// Display answer
console.log("Answer: ", answer);