class Solution:
    def longestMountain(self, A: List[int]) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        if len(A) < 3: return 0
        
        maxLen = 0
        for i in range(1, len(A)-1):
            left, right = i - 1, i + 1
            if (A[left] < A[i]) and (A[i] > A[right]):
                while left > 0 and A[left-1] < A[left]:
                    left -= 1
                while right < len(A)-1 and A[right] > A[right+1]:
                    right += 1
                maxLen = max(maxLen, right - left + 1)
        return maxLen
