public class NumberPalindrome {
    
    public static boolean isPalindrome(int number) {
        int copyNumber = Math.abs(number);
        int reverseNumber = 0;
        int i = 0;
        while (copyNumber > 0) {
            int lastDigit = copyNumber % 10;
            copyNumber /= 10;
            reverseNumber = reverseNumber * 10 + lastDigit;
            i++;
            //System.out.println(number);
        }
        System.out.println(reverseNumber);
        return reverseNumber == Math.abs(number);
    }
}
