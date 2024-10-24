// function removeElement() {
//   let arr = [0, 1, 2, 2, 3, 0, 4, 2];
//   let val = 2;
//   let temp = [];

//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] !== val) {
//       temp.push(arr[i]);
//     }
//   }

//   console.log(temp.length);
// }
function removeElement() {
  let arr = [3, 2, 2, 3];
  let val = 3;
  let temp = 0;

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== val) {
      arr[temp] = arr[i]; // here result value should be [2,2] hence i am implementing this
      temp++;
    }
  }
  console.log(temp);
}
removeElement();
