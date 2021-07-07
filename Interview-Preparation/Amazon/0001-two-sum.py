class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,num in enumerate(nums):
            need = target - num
            if need in d:
                return (d[need], i)
            else:
                d[num] = i
        return (-1, -1)

    
