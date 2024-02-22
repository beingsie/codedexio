// Create function with 1 parameter
function relativityTheory(mass) { // Mass being the parameter
  // Speed of light (sol)
  const sol = 3e8 ** 2; 
  // E = mc²
  let e = mass * sol;
  // Return output
  return e;
}
// Print to console and insert parameter
console.log(relativityTheory(59.4206));
