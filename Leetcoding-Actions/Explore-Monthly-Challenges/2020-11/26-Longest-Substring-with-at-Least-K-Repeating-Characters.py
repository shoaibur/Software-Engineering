class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        '''
        T: O(n) and S: O(1)
        '''
        n = len(s)
        if n == 0 or n < k: return 0
        if k <= 1: return n
        
        charCounts = Counter(s)
        l = 0
        while l < n and charCounts[s[l]] >= k:
            l += 1
        if l >= n - 1: return l
        
        ls1 = self.longestSubstring(s[:l], k)
        while l < n and charCounts[s[l]] < k:
            l += 1
        ls2 = self.longestSubstring(s[l:], k) if l < n else 0
        
        return max(ls1, ls2)
