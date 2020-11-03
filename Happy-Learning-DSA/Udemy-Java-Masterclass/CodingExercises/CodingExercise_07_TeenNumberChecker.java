public class TeenNumberChecker {
    public static boolean hasTeen(int x, int y, int z) {
        return isTeen(x) || isTeen(y) || isTeen(z);
    }
    
    public static boolean isTeen(int x) {
        return (x >= 13 && x <= 19);
    }
}
