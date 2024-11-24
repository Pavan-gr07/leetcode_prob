function square(n) {
  // var lo = 0,
  //   hi = number;
  // while (lo <= hi) {
  //   var mid = Math.floor((lo + hi) / 2);

  //   if (mid * mid > number) hi = mid - 1;
  //   else lo = mid + 1;
  // }
  // return hi;

  var avg = (a, b) => (a + b) / 2,
    c = 5,
    b;
  for (let i = 0; i < 20; i++) {
    b = n / c;
    c = avg(b, c);
  }
  const result = c - Math.floor(c) === 0;
  return result;
}

console.log(square(8));
