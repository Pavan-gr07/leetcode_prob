const nums = [2, 5, 5, 11];
const target = 10;

function twoSum(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = i+1; j < nums.length; j++) {
      console.log(nums[i] + nums[j]);
      if (nums[i] + nums[j] === target) {
        return [i, j];
      }
    }
  }
}

console.log(twoSum(nums, target));
