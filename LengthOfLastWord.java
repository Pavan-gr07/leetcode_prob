
import java.util.Arrays;

public class LengthOfLastWord {

    public static int wordLength(String s) {
        String str = s.trim();
        String[] words = str.split("");
        System.out.println(Arrays.toString(words));

        if (str.length() == 1) {
            return str.length();
        }
        int count = 0;
        for (int i = str.length() - 1; i >= 0; i--) {
            if (str.charAt(i) != ' ') {
                count++;
            } else {
                break;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        int result = wordLength("Hello World");
        System.out.println(result);
    }
}
