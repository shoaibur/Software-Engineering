class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        nlow, nhigh = len(str(low)), len(str(high))
        s = '123456789'
        
        result = []
        for n in range(nlow, nhigh+1):
            for i in range(9-n+1):
                num = int(s[i:i+n])
                if num < low: continue
                if num > high: break
                result.append(num)
        return result
