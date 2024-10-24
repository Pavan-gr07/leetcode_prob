// function plusOne(arr) {
//   let val = arr.join("");

//   let sum = Number(val) + 1;
//   return Array.from(String(sum), Number);
//   // sum.toString().split("").map(Number) this also work fine
//   // convert number to string
//   // spli("") -> string to an array
//   // map(Number) -> convert array element to a number
// }
function plusOne(digits) {
  for (let i = digits.length - 1; i >= 0; i--) {
    // Start from the last digit
    if (digits[i] + 1 !== 10) {
      // If the current digit + 1 is NOT 10
      digits[i] += 1; // Simply increment the digit
      return digits; // Return the updated digits
    }
    digits[i] = 0; // If the current digit + 1 is 10, set it to 0
    if (i === 0) {
      // If we're at the first digit and it's 9
      digits.unshift(1); // Add 1 at the beginning
      return digits; // Return the result
    }
  }
}

console.log(plusOne([1, 2, 3]));
