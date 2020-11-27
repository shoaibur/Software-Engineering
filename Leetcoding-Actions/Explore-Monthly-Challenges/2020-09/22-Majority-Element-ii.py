class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        result = []
        for num in counter:
            if counter[num] > len(nums) // 3:
                result.append(num)
        
        return result
