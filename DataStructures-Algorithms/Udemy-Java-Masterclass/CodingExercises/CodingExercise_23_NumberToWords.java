import java.util.HashMap;

public class NumberToWords {
    
    public static void numberToWords(int number) {
        if (number < 0) {
            System.out.println("Invalid Value");
            return;
        }
        if (number == 0){
            System.out.println("Zero");
            return;
        }
        int nDigits = getDigitCount(number);
        int reversedNumber = reverse(number);
        int nDigitsReverse = getDigitCount(reversedNumber);

        String[] numToWords = new String[] {"Zero", "One", "Two", "Three",
                "Four", "Five", "Six", "Seven", "Eight", "Nine"};
        HashMap<Integer, String> map = new HashMap<>();
        for (int i = 0; i < 10; i++)
            map.put(i, numToWords[i]);
        while (reversedNumber > 0) {
            int digit = reversedNumber % 10;
            reversedNumber /= 10;
            System.out.println(map.get(digit));
        }
        for (int i = 0; i < (nDigits - nDigitsReverse); i++)
            System.out.println("Zero");
    }

    public static int getDigitCount(int number) {
        if (number < 0) return -1;
        if (number == 0) return 1;
        int digitCount = 0;
        while (number > 0) {
            number /= 10;
            digitCount++;
        }
        return digitCount;
    }

    public static int reverse(int number) {
        boolean negative = false;
        if (number < 0) {
            number = Math.abs(number);
            negative = true;
        }
        int reversedNumber = 0;
        while (number > 0) {
            int digit = number % 10;
            number /= 10;
            reversedNumber = reversedNumber * 10 + digit;
        }
        if (negative)
            return -1 * reversedNumber;
        return reversedNumber;
    }
}
