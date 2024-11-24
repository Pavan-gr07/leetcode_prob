function sumOfOddNum(n) {
  let sum = 0;
  for (let i = 1; i <= n + (n - 1); i++) {
    if (i % 2 !== 0) {
      sum += i;
      console.log(i);
    }
  }
  return sum;
}

console.log(sumOfOddNum(2));
