function palindromeString(s) {
  // let start = 0;
  // let end = s.length - 1;
  // while (start < end)
  // {
  //     if (start < end&&s[start])
  //     {

  //     }
  // }

  const filteredChars = s.toLowerCase().replace(/[^a-z0-9]/g, "");
  console.log(filteredChars);
  return filteredChars === filteredChars.split("").reverse().join("");
}
console.log(palindromeString("A man, a plan, a canal: Panama"));
