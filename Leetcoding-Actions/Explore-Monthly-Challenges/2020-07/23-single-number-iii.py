class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        result = set()
        
        for num in nums:
            if num in result:
                result.remove(num)
            else:
                result.add(num)
        
        result = list(result) + [0] * (2-len(result))
        return result
