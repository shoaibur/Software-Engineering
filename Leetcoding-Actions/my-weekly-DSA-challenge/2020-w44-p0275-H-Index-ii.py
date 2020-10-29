class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        T: O(log n) and S: O(1)
        '''
        n = len(citations)
        lo, hi = 0, n - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if citations[mid] >= n - mid:
                hi = mid - 1
            else:
                lo = mid + 1
        return n - lo
        
        '''
        T: O(n) and S: O(1)
        
        nPaper = 0
        hindex = 0
        
        for i in range(len(citations)-1, -1, -1):
            citation = citations[i]
            nPaper += 1
            
            if citation >= nPaper:
                hindex = nPaper
            
        return hindex
        '''
