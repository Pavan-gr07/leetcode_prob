function firstOccurence(haystack, needle) {
  for (let i = 0; i <= haystack.length - needle.length; i++) {
    console.log(haystack.substring(i, needle.length));
    if (haystack.substring(i, i + needle.length) === needle) {
      return i;
    }
  }
  return -1;
}

console.log(firstOccurence("mississippi", "issip"));
// 0->11-5=6->missi
//1 ->11-5=6->issis
//2 ->11-5=6->ssisi
//3 ->11-5=6->sisis
//4 ->11-5=6->issip
