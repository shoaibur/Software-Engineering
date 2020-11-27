class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums: return []
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        res = []
        for num in d:
            if d[num] > 1:
                res.append(num)
        return res
