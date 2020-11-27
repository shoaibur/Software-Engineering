class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        T: O(n)
        S: O(1)
        """
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        
# Solution 2: Same as above, but using reverse array function explicitly
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        T: O(n)
        S: O(1)
        """
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i, j = i + 1, j - 1
                
        k = k % len(nums)
        reverse(nums, 0, len(nums)-1)
        reverse(nums, 0,k-1)
        reverse(nums, k, len(nums)-1)
        
