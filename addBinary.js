// function addBinary(a, b) {
//   const a1 = parseInt(a, 10);
//   console.log(a1);
//   const a2 = parseInt(b, 2);
//   return (a1 + a2).toString(2);
// }
function addBinary(a, b) {
  let result = ""; // Store the result binary string
  let carry = 0; // Store carry
  let i = a.length - 1;
  let j = b.length - 1;

  // Traverse both strings from the end to the beginning
  while (i >= 0 || j >= 0 || carry > 0) {
    const bitA = i >= 0 ? parseInt(a[i], 10) : 0; // Get bit from a or 0 if out of bounds
    const bitB = j >= 0 ? parseInt(b[j], 10) : 0; // Get bit from b or 0 if out of bounds

    const sum = bitA + bitB + carry; // Sum the bits and carry
    console.log(sum, "sum");
    result = (sum % 2) + result; // Append the result bit to the front
    carry = Math.floor(sum / 2); // Update carry
    console.log(carry);

    i--; // Move to the next bit
    j--;
  }

  return result;
}

// They are 0 + 0 = 0, 0 + 1 = 1, 1 + 0 = 1, and 1 + 1 = 10
console.log(addBinary("1010", "1011"));
