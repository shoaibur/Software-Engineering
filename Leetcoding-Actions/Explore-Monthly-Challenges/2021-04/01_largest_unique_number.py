class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        num2count = {}
        for num in A:
            num2count[num] = num2count.get(num, 0) + 1
            
        max_num = -1
        for num, count in num2count.items():
            if count == 1:
                max_num = max(max_num, num)
        
        return max_num
