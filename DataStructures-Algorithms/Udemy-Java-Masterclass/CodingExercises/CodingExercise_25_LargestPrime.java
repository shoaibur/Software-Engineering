public class LargestPrime {
    public static int getLargestPrime(int number) {
        if (number < 2) return -1;

        int maxPrime = 0;
        for (int i = 1; i <= number; i++) {
            // Is i a factor?
            if (number % i == 0) {
                // Is i prime?
                boolean isPrime = true;
                for (int j = 2; j < i/2+1; j ++) {
                    if (i % j == 0) {
                        isPrime = false;
                        break;
                    }
                }
                if (isPrime)
                    maxPrime = Math.max(maxPrime, i);
            }
        }
        return maxPrime;
    }
}
