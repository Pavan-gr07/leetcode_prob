function searchInsertPos(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] === target) {
      return i;
    } else if (i > 0 && target > nums[i - 1] && target < nums[i]) {
      return i;
    } else if (target > nums[nums.length - 1]) {
      return nums.length;
    }
  }
  //   return nums.length;
  return 0;
}

console.log(searchInsertPos([1, 3, 5, 6], 5));
// nums = [1,3,5,6], target = 5 --2
// nums = [1,3,5,6], target = 2 --1
// Input: nums = [1,3,5,6], target = 7 --4
