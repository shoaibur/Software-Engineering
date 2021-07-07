class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        pos_len, neg_len = 1, 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                pos_len = neg_len + 1
            elif nums[i] < nums[i-1]:
                neg_len = pos_len + 1
                
        return max(pos_len, neg_len)
