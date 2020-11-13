public class MinutesToYearsDaysCalculator {
    
    public static void printYearsAndDays(long minutes) {
        if (minutes < 0) {
            System.out.println("Invalid Value");
        } else {
            int minutesInOneYear = 365 * 24 * 60;
            int minutesInOneDay = 24 * 60;
            long years = minutes / minutesInOneYear;
            long days = (minutes - years * minutesInOneYear) / minutesInOneDay;
            System.out.println(minutes + " min = " + years + " y and " + days + " d");
        }
    }
}
