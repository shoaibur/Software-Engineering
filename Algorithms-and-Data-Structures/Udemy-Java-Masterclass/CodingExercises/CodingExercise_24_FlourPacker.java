public class FlourPacker {
    
    public static boolean canPack(int bigCount, int smallCount, int goal) {
        if (bigCount < 0 || smallCount < 0 || goal < 0)
            return false;
        while (bigCount > 0 && goal >= 5) {
            bigCount -= 1;
            goal -= 5;
        }
        return smallCount >= goal;
    }
}
