public class SumOddRange {
    
    public static boolean isOdd(int number) {
        if (number <= 0) return false;
        return number % 2 != 0;
    }
    
    public static int sumOdd(int start, int end) {
        if (end < start || start < 0 || end < 0)
            return -1;
            
        int sum = 0;
        for (int num = start; num <= end; num++) {
            if (isOdd(num)) {
                sum += num;
            }
        }
        return sum;
    }
}
