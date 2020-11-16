class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
            
        d = {}
        for num in nums2:
            d[num] = d.get(num, 0) + 1
        
        for num in nums1:
            if num in d and d[num] > 0:
                result.append(num)
                d[num] -= 1
        return result
