class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        1 2 4 8 5 2 <-- increasing seq from right
            i   j
        1 2 5 8 4 2 <-- swap
        1 2 5 2 4 8 <-- reverse right
        
        Speical cases: i could be 0 at each of following cases
        3 2 1
        2 3 1
        
        T: O(n)
        S: O(1)
        '''
        n = len(nums)
        if n <= 1: return
        
        # Increasing sequence from right
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                break
        # Take care of special case
        if i == 0 and nums[0] > nums[1]:
            nums[:] = nums[::-1]
            return
        # Find num in right seq larger than num[i]        
        for j in range(n-1, i, -1):
            if nums[j] > nums[i]:
                break
        # Swap
        nums[i], nums[j] = nums[j], nums[i]
        # Reverse right part
        nums[i+1:] = nums[i+1:][::-1]
        return
