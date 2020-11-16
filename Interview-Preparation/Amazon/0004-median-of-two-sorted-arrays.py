class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = self.mergeSortedLists(nums1, nums2)
        print(nums)
        n = len(nums)
        if n % 2:
            return nums[n//2]
        return 0.5 * ( nums[n//2-1] + nums[n//2] )
    
    def mergeSortedLists(self, nums1, nums2):
        if not nums1: return nums2
        if not nums2: return nums1
        
        nums = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        nums += nums1[i:]
        nums += nums2[j:]
        
        return nums
