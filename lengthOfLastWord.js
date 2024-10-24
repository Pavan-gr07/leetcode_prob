function lengthOfLastWord(s) {
  const str = s.trim();
  if (str.length == 1) {
    return str.length;
  }
  let temp = 0;
  for (let i = str.length - 1; i >= 0; i--) {
    if (str[i] !== " ") {
      temp++;
    } else {
      break;
    }
  }
  return temp;
}

console.log(lengthOfLastWord("Hello World"));
