import java.util.Scanner;

public class InputCalculator {
    
    public static void inputThenPrintSumAndAverage() {
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        double count = 0;
        while (sc.hasNextInt()) {
            sum += sc.nextInt();
            count += 1;
        }
        long avg = (long) (Math.round(sum / count));
        System.out.println("SUM = " + sum + " AVG = " + avg);
    }
}
