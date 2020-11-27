class Solution:
    def hIndex(self, citations: List[int]) -> int:
    
        if not citations: return 0
        citations.sort(reverse=True)
        
        i = 0
        while i < len(citations) and citations[i] > i:
            i += 1
        return i
