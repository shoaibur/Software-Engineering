class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = True
        
        pos = 1
        while True:
            if pos not in d:
                return pos
            pos += 1
        return
