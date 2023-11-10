// Currencies
let chineseYuan = 560
let japaneseYen = 2455
let southKoreanWon = 3280

// Exchange rates to USD
let yuanExchangeRate = 0.14;
let yenExchangeRate = 0.0067;
let wonExchangeRate = 0.00074;

// Calculate left over foreign currencies to USD
let calcYuan = chineseYuan * yuanExchangeRate;
let calcYen = japaneseYen * yenExchangeRate;
let calcWon = southKoreanWon * wonExchangeRate;

// Calculate total currency in USD
let totalCurrency = calcYuan + calcYen + calcWon;

// Print total USD currency
console.log(totalCurrency)