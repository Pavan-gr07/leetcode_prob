function divisiable() {
  let arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9];
  let k = 5; // Target value for divisibility

  console.log(`Pairs with sum divisible by ${k}:`);

  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length; j++) {
      let sum = arr[i] + arr[j];

      if (sum % k === 0) {
        console.log(`(${arr[i]}, ${arr[j]})`);
      }
    }
  }
}

divisiable();
