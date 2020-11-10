import java.util.HashMap;

public class LastDigitChecker {
    
    public static boolean hasSameLastDigit(int x, int y, int z) {
        if (!isValid(x) || !isValid(y) || !isValid(z))
            return false;
        HashMap<Integer, Boolean> map = new HashMap<>();
        int[] lastDigits = new int[3];

        lastDigits[0] = x % 10;
        lastDigits[1] = y % 10;
        lastDigits[2] = z % 10;
        for (int digit : lastDigits) {
            if (map.containsKey(digit))
                return true;
            map.put(digit, true);
        }
        return false;
    }

    public static boolean isValid(int num) {
        return num >= 10 && num <= 1000;
    }
}
