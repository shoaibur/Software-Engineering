public class FirstLastDigitSum {
    
    public static int sumFirstAndLastDigit(int number) {
        if (number < 0) return -1;
        
        int lastDigit = number % 10;
        number /= 10;
        if (number == 0)
            return lastDigit * 2;
        
        int firstDigit = 0;
        while (number > 0) {
            firstDigit = number % 10;
            number /= 10;
        }
        return firstDigit + lastDigit;
    }
}
