class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        '''
        T: O(n) and S: O(1)
        '''
        n = len(nums)
        
        for i in range(n):
            if nums[i] == 1:
                break
        
        for j in range(i+1, n):
            if nums[j] == 1:
                if j - i - 1 < k:
                    return False
                i = j
                
        return True
