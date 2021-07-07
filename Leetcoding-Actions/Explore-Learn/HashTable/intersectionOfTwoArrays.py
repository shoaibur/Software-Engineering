class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)
        nums2Set = set(nums2)
        result = set()
        for num in nums1Set:
            if num in nums2Set:
                result.add(num)
        return result
