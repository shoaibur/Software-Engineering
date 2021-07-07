class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numDict = {}
        for num in nums:
            if num in numDict:
                return True
            else:
                numDict[num] = True
        return False
