class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = set()
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        
        nums2 = set(nums2)
        for num in nums1:
            if num in nums2:
                result.add(num)
        return result
