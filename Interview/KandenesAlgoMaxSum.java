package Interview;

public class KandenesAlgoMaxSum {

     public static int  maxNumber(int[] arr){
        int max_sum = Integer.MIN_VALUE;
        int cur_sum = 0;
        for(int i =0;i<arr.length;i++)
        {
            cur_sum += arr[i];
            max_sum = Math.max(cur_sum,max_sum);
            if(cur_sum < 0)
            {
                cur_sum = 0;
            }

        }
        return max_sum;
     }
    public static void main(String[] args) {
        System.out.println(maxNumber(new int[]{ 2, 3, -8, 7, -1, 2, 3}));
    }
}