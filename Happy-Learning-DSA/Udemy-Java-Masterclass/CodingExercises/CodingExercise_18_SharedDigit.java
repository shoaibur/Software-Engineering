import java.util.HashMap;

public class SharedDigit {
    
    public static boolean hasSharedDigit(int x, int y) {
        if (x < 10 || x > 99 || y < 10 || y > 99)
            return false;

        HashMap<Integer, Boolean> map = new HashMap<>();
        while (x > 0) {
            int digit = x % 10;
            map.put(digit, true);
            x /= 10;
        }

        while (y > 0) {
            int digit = y % 10;
            if (map.containsKey(digit))
                return true;
            y /= 10;
        }

        return false;
    }
}
