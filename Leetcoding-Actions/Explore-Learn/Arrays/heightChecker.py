class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        '''
        T: O(n log n) and S: O(1)
        '''
        count = 0
        s = sorted(heights)
        for i in range(len(s)):
            if s[i] != heights[i]:
                count += 1
        return count
