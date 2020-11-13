public class LeapYear {
    
    public static boolean isLeapYear(int year) {
        if (year < 1 || year > 9999) {
            return false;
        }
        if (year % 4 != 0) {
            return false;
        } else if (year % 25 != 0) {
            return true;
        } else if (year % 16 != 0) {
            return false;
        }
        return true;
    }
}
