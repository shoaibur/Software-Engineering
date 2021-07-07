class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals
        
        intervals.sort()
        
        def overlap(i1, i2):
            isoverlap, merged = False, []
            if i1[1] >= i2[0]:
                isoverlap = True
                merged = [min(i1[0], i2[0]), max(i1[1], i2[1])]
            return isoverlap, merged
        
        result = [intervals[0]]
        i1 = result[-1]
        
        for i2 in intervals[1:]:
            isoverlap, merged = overlap(i1, i2)
            if isoverlap:
                result[-1] = merged
                i1 = result[-1]
            else:
                result.append(i2)
                i1 = i2
        return result
