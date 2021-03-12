class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        '''
        T: O(nk) and S: O(nk)
        '''
        checked = {s[i-k:i] for i in range(k, len(s)+1)}
        
        return len(checked) == (1 << k)
