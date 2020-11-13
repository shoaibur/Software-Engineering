public class DecimalComparator{
    
    public static boolean areEqualByThreeDecimalPlaces(double x, double y) {
        x = (int) (x * 1000);
        y = (int) (y * 1000);
        return x == y;
    }
}
