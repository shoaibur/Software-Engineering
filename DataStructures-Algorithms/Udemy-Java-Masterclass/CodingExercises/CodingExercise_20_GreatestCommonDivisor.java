public class GreatestCommonDivisor {
    
    public static int getGreatestCommonDivisor(int first, int second) {
        if (first < 10 || second < 10) return -1;
        if (first > second) {
            int temp = first;
            first = second;
            second = temp;
        }
        int prevFirst = first;
        while (first > 0) {
            prevFirst = first;
            first = second % first;
            second = prevFirst;
        }
        return prevFirst;
    }
}
