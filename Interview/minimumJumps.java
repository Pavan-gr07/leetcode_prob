package Interview;

public class minimumJumps {
    public static int minJumps(int[] arr) {
        int n = arr.length;
        if (n <= 1) return 0;             // Already at the end
        if (arr[0] == 0) return -1;       // Can't move anywhere
    
        int maxReach = arr[0];           // Farthest index reachable
        int steps = arr[0];              // Steps you can still take
        int jumps = 1;                   // You start by making 1 jump
    
        for (int i = 1; i < n; i++) {
            if (i == n - 1) return jumps;
    
            maxReach = Math.max(maxReach, i + arr[i]);  // update maxReach
            steps--;   // we use a step to move to index i
    
            if (steps == 0) {
                jumps++;       // time to jump
                if (i >= maxReach) return -1;  // cannot go further
                steps = maxReach - i;   // reset steps
            }
        }
    
        return -1;
    }
    
    
    public static void main(String[] args) {
        System.out.print(minJumps(
            new int[]{9 ,10, 1, 2, 3, 4, 8, 0, 0, 0, 0, 0, 0, 0, 1}
        ));
    }
}
