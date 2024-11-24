
class PalindromeString {

    static boolean paliString(String s) {
        int start = 0;
        char[] str = s.toCharArray();
        int end = str.length - 1;

        while (start < end) {

            while (start < end && !Character.isLetterOrDigit(str[start])) {
                start++;
                System.out.println(start);
            }
            while (start < end && !Character.isLetterOrDigit(str[end])) {
                end--;
            }
            if (start < end && Character.toLowerCase(str[start]) != Character.toLowerCase(str[end])) {
                return false;
            }

            start++;
            end--;
        }
        return true;
    }

    public static void main(String[] args) {
        // System.out.println(Character.isLetterOrDigit(':'));
        boolean result = paliString("A man, a plan, a canal: Panama");
        System.out.println(result);
    }
}

// i/p A man, a plan, a canal: Panama->amanaplanacanalpanama
// o/p true
