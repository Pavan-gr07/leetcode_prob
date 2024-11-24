
public class FrquencyOfNumbers {

    public static void main(String[] args) {
        int[] arr = {1, 2, 23, 4, 35, 5, 4, 35, 36, 2, 2};
        int maxNumber = arr.length; // Maximum number in the array
        int[] frequency = new int[maxNumber + 1]; // Array to store frequencies

        // Count frequencies
        for (int num : arr) {
            frequency[num]++;
        }
        System.out.println(frequency);
        // Print the result
        System.out.println("{");
        for (int i = 1; i <= maxNumber; i++) {
            if (frequency[i] > 0) {
                System.out.println(i + ": " + frequency[i] + ",");
            }
        }
        System.out.println("}");
    }
}
