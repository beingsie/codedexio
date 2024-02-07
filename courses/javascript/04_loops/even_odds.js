// Iterate from 0-4
for (let i = 0; i <5; i++) {
  // Skip iteration for 1 using `continue`
  if (i == 1) {
    continue;
  }
  // Print results
  console.log(i);
}

// Iterate from 1-5
for (let i = 0; i < 5; i++) {
  // If iteration is equal to 3 break from loop
  if (i == 3) {
    break;
  }
  // Print results
  console.log(i);
}

// Iterate from 1-50
for (i = 1; i <= 50; i++) {
  // Skip odd numbers
  if ((i % 2) == 1) {
    continue;
  }
  // Break & log to console if 42 
  if (i == 42) {
    break;
  }
  // Print results
  console.log(i);
}
