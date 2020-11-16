class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d = {}
        for num in nums1:
            d[num] = d.get(num, 0) + 1
        
        result = []
        for num in nums2:
            if num in d and d[num] > 0:
                d[num] -= 1
                result.append(num)
        return result
