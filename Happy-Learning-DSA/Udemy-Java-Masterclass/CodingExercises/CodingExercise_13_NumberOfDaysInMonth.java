public class NumberOfDaysInMonth {
    
    public static boolean isLeapYear(int year) {
        if (year < 1 || year > 9999) return false;
        return (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    }

    public static int getDaysInMonth(int month, int year) {
        if (month < 1 || month > 12 || year < 1 || year > 9999)
            return -1;
        int[] daysInMonth = new int[] {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        if (isLeapYear(year) && month == 2)
            return 29;
        return daysInMonth[month - 1];
    }
}
