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

// Horoscope symbols with emojis
let capricornSymbol = "♑️";
let aquariusSymbol = "♒️";
let piscesSymbol = "♓️";
let ariesSymbol = "♈️";
let geminiSymbol = "♊️";
let cancerSymbol = "♋️";
let leoSymbol = "♌️";
let virgoSymbol = "♍️";
let libraSymbol = "♎️";
let scorpioSymbol = "♏️";
let sagittariousSymbol = "♐️";

let monthsTotal = 12;
// Loop through all 12 months
while (true) {
  // Default message
  let defaultMessage = "You're horoscope is";
  // Match user birth month to its respective horoscope
  if (userBirthMonth === 1) {
    console.log(defaultMessage, chalk.cyanBright("Capricorn"), capricornSymbol);
    break;
  } else if (userBirthMonth === 2) {
    console.log(defaultMessage, chalk.blue("Aquarius"), aquariusSymbol);
    break;
  } else if (userBirthMonth === 3) {
    console.log(defaultMessage, chalk.cyan("Pisces"), piscesSymbol);
    break;
  } else if (userBirthMonth === 4) {
    console.log(defaultMessage, chalk.green("Aries"), ariesSymbol);
    break;
  } else if (userBirthMonth === 5) {
    console.log(defaultMessage, chalk.yellow("Gemini"), geminiSymbol);
    break;
  } else if (userBirthMonth === 6) {
    console.log(defaultMessage, chalk.red("Cancer"), cancerSymbol);
    break;
  } else if (userBirthMonth === 7) {
    console.log(defaultMessage, chalk.blueBright("Leo"), leoSymbol);
    break;
  } else if (userBirthMonth === 8) {
    console.log(defaultMessage, chalk.greenBright("Virgo"), virgoSymbol);
    break;
  } else if (userBirthMonth === 9) {
    console.log(defaultMessage, chalk.yellowBright("Libra"), libraSymbol);
    break;
  } else if (userBirthMonth === 10) {
    console.log(defaultMessage, chalk.redBright("Scorpio"), scorpioSymbol);
    break;
  } else {
    console.log(defaultMessage, chalk.magentaBright("Sagittarius"), sagittariousSymbol);
    break;
  }
}
