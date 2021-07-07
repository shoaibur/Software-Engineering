class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cumSum = 0
        cumSumDict = {}
        for num in nums:
            cumSum += num
            if cumSum == k:
                count += 1
            if cumSum - k in cumSumDict:
                count += cumSumDict[cumSum-k]
            cumSumDict[cumSum] = cumSumDict.get(cumSum, 0) + 1
        return count
