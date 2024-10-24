public class SearchInsertPos {


    public static int occurence(int[] nums,int target)
    {
        for (int i = 0; i < nums.length; i++)
        {
            if(nums[i]==target)
            {
                return i;
            }else if(nums[i-1]<target&&nums[i]>target)
            {
                return i;
            }else if(target>nums[nums.length-1])
            {
                return nums.length;
            }
        }

        return 0;
    }
    public static void main(String[] args) {
        int result = occurence(new int[]{1, 3, 5, 6}, 5);
        System.out.println(result);
    }
}
