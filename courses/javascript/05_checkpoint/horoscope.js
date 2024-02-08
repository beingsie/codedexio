// Require chalk
import chalk from "chalk";

// User birth month
let userBirthMonth = Math.floor(Math.random() * 10);

// Horoscopes & their month number
let capricorn = 1;
let aquarius = 2;
let pisces = 3;
let aries = 4;
let gemini = 5;
let cancer = 6;
let leo = 7;
let virgo = 8;
let libra = 9;
let scorpio = 10;
let sagittarious = 11;

let monthsTotal = 12;
// Loop through all 12 months
while (true) {
    // Default message
    let defaultMessage = "You're horoscope is";
    // Match user birth month to its respective horoscope
    if (userBirthMonth === 1) {
        console.log(defaultMessage, "\x1b[36mCapricorn\x1b[0m");
        break;
    } else if (userBirthMonth === 2) {
        console.log(defaultMessage, "Aquarius");
        break;
    } else if (userBirthMonth === 3) {
        console.log(defaultMessage, "Pisces");
        break;
    } else if (userBirthMonth === 4) {
        console.log(defaultMessage, "Aries");
        break;
    } else if (userBirthMonth === 5) {
        console.log(defaultMessage, "Gemini");
        break;
    } else if (userBirthMonth === 6) {
        console.log(defaultMessage, "Cancer");
        break;
    } else if (userBirthMonth === 7) {
        console.log(defaultMessage, "Leo");
        break;
    } else if (userBirthMonth === 8) {
        console.log(defaultMessage, "Virgo");
        break;
    } else if (userBirthMonth === 9) {
        console.log(defaultMessage, "Libra");
        break;
    } else if (userBirthMonth === 10) {
        console.log(defaultMessage, "Scorpio");
        break;
    } else {
        console.log(defaultMessage, "Sagittarious");
        break;
    }
}