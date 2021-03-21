class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        digit_counts_N = collections.Counter(str(N))
        
        for i in range(32):
            power_of_2 = 1 << i
            digit_counts_power_of_2 = collections.Counter(str(power_of_2))
            
            if digit_counts_power_of_2 == digit_counts_N:
                return True
        
        return False
