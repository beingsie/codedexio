// Require chalk
import chalk from "chalk";

// User birth month (0-12)
let userBirthMonth = Math.floor(Math.random() * 13);

// Horoscopes & their month number
let capricorn = 0;
let aquarius = 1;
let pisces = 2;
let aries = 3;
let taurus = 4;
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
let taurusSymbol = "♉";
let geminiSymbol = "♊️";
let cancerSymbol = "♋️";
let leoSymbol = "♌️";
let virgoSymbol = "♍️";
let libraSymbol = "♎️";
let scorpioSymbol = "♏️";
let sagittariousSymbol = "♐️";

// Zodiac personality traits
let capricornPersonality = "Capricorn is climbing the mountain straight to the top and knows that patience, perseverance, and dedication is the only way to scale. The last earth sign of the zodiac, Capricorn, is represented by the sea-goat, a mythological creature with the body of a goat and the tail of a fish. Accordingly, Capricorns are skilled at navigating both the material and emotional realms.";
let aquariusPersonality = "Innovative, progressive, and shamelessly revolutionary, Aquarius is represented by the water bearer, the mystical healer who bestows water, or life, upon the land. Accordingly, Aquarius is the most humanitarian astrological sign. At the end of the day, Aquarius is dedicated to making the world a better place.";
let piscesPersonality = "Pisces is the most intuitive, sensitive, and empathetic sign of the entire zodiac — and that’s because it’s the last of the last. As the final sign, Pisces has absorbed every lesson — the joys and the pain, the hopes and the fears — learned by all of the other signs. It's symbolized by two fish swimming in opposite directions, representing the constant division of Pisces' attention between fantasy and reality.";
let ariesPersonality = "Aries loves to be number one. Naturally, this dynamic fire sign is no stranger to competition. Bold and ambitious, Aries dives headfirst into even the most challenging situations—and they'll make sure they always come out on top!";
let taurusPersonality = "Taurus is an earth sign represented by the bull. Like their celestial spirit animal, Taureans enjoy relaxing in serene, bucolic environments surrounded by soft sounds, soothing aromas, and succulent flavors.";
let geminiPersonality = "Spontaneous, playful, and adorably erratic, Gemini is driven by its insatiable curiosity. Appropriately symbolized by the celestial twins, this air sign was interested in so many pursuits that it had to double itself. You know, NBD!";
let cancerPersonality = "Cancer seamlessly weaves between the sea and shore representing Cancer’s ability to exist in both emotional and material realms. Cancers are highly intuitive and their psychic abilities manifest in tangible spaces. But—just like the hard-shelled crustaceans—this water sign is willing to do whatever it takes to protect itself emotionally. In order to get to know this sign, you're going to need to establish trust!";
let leoPersonality = "Passionate, loyal, and infamously dramatic, Leo is represented by the lion and these spirited fire signs are the kings and queens of the celestial jungle. They're delighted to embrace their royal status: Vivacious, theatrical, and fiery, Leos love to bask in the spotlight and celebrate… well, themselves.";
let virgoPersonality = "Virgos are logical, practical, and systematic in their approach to life. Virgo is an earth sign historically represented by the goddess of wheat and agriculture, an association that speaks to Virgo's deep-rooted presence in the material world. This earth sign is a perfectionist at heart and isn’t afraid to improve skills through diligent and consistent practice.";
let libraPersonality = "Balance, harmony, and justice define Libra energy. As a cardinal air sign, Libra is represented by the scales (interestingly, the only inanimate object of the zodiac), an association that reflects Libra's fixation on establishing equilibrium. Libra is obsessed with symmetry and strives to create equilibrium in all areas of life — especially when it comes to matters of the heart";
let scorpioPersonality = "Elusive and mysterious, Scorpio is one of the most misunderstood signs of the zodiac. Scorpio is a water sign that uses emotional energy as fuel, cultivating powerful wisdom through both the physical and unseen realms. In fact, Scorpio derives its extraordinary courage from its psychic abilities, which is what makes this sign one of the most complicated, dynamic signs of the zodiac.";

let monthsTotal = 12;
// Loop through all 12 months
while (true) {
  // Default message
  let defaultMessage = "You're horoscope is";
  // Match user birth month to its respective horoscope
  if (userBirthMonth === 0) {
    console.log(defaultMessage, chalk.cyanBright("Capricorn"), capricornSymbol);
    console.log(chalk.dim(capricornPersonality));
    break;
  } else if (userBirthMonth === 1) {
    console.log(defaultMessage, chalk.blue("Aquarius"), aquariusSymbol);
    console.log(chalk.dim(aquariusPersonality));
    break;
  } else if (userBirthMonth === 2) {
    console.log(defaultMessage, chalk.cyan("Pisces"), piscesSymbol);
    console.log(chalk.dim(piscesPersonality));
    break;
  } else if (userBirthMonth === 3) {
    console.log(defaultMessage, chalk.green("Aries"), ariesSymbol);
    console.log(chalk.dim(ariesPersonality));
    break;
  } else if (userBirthMonth === 4) {
    console.log(defaultMessage, chalk.green("Taurus"), taurusSymbol);
    console.log(chalk.dim(taurusPersonality));
    break;
  } else if (userBirthMonth === 5) {
    console.log(defaultMessage, chalk.yellow("Gemini"), geminiSymbol);
    console.log(chalk.dim(geminiPersonality));
    break;
  } else if (userBirthMonth === 6) {
    console.log(defaultMessage, chalk.red("Cancer"), cancerSymbol);
    console.log(chalk.dim(cancerPersonality));
    break;
  } else if (userBirthMonth === 7) {
    console.log(defaultMessage, chalk.blueBright("Leo"), leoSymbol);
    console.log(chalk.dim(leoPersonality));
    break;
  } else if (userBirthMonth === 8) {
    console.log(defaultMessage, chalk.greenBright("Virgo"), virgoSymbol);
    console.log(chalk.dim(virgoPersonality));
    break;
  } else if (userBirthMonth === 9) {
    console.log(defaultMessage, chalk.yellowBright("Libra"), libraSymbol);
    console.log(chalk.dim(libraPersonality));
    break;
  } else if (userBirthMonth === 10) {
    console.log(defaultMessage, chalk.redBright("Scorpio"), scorpioSymbol);
    console.log(chalk.dim(scorpioPersonality));
    break;
  } else {
    console.log(defaultMessage, chalk.magentaBright("Sagittarius"), sagittariousSymbol);
    console.log(chalk.dim(sagittariousPersonality));
    break;
  }
}
