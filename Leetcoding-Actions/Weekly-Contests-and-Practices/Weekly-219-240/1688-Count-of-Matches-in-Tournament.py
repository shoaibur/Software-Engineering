class Solution:
    def numberOfMatches(self, n: int) -> int:
        count = 0
        while n >= 2:
            count += n // 2
            print(count)
            if n % 2:
                n = n // 2 + 1
            else:
                n = n // 2
            
        return count

