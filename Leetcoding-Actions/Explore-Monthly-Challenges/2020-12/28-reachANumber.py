class Solution:
    def reachNumber(self, target: int) -> int:
        
        target = abs(target)
        step, summ = 0, 0
        
        while summ < target or (summ - target) % 2:
            step += 1
            summ += step
        
        return step
