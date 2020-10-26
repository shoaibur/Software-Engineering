class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        T: O(n log n) and S: O(n)
        '''
        n = len(intervals)
        if n <= 1: return intervals
        
        def isOverlap(i1, i2):
            overlap, merged = False, []
            if i1[1] >= i2[0]:
                overlap = True
                merged = [min(i1[0], i2[0]), max(i1[1], i2[1])]
            return overlap, merged
        
        intervals.sort()
        result = [intervals[0]]
        i1 = result[-1]
        for i2 in intervals[1:]:
            overlap, merged = isOverlap(i1, i2)
            if overlap:
                result[-1] = merged
            else:
                result.append(i2)
            i1 = result[-1]
        
        return result
