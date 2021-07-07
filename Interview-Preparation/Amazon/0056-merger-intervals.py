class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals
        
        def isoverlap(int1, int2):
            overlap = False
            merged = None
            if int1[1] >= int2[0]:
                overlap = True
                merged = (min(int1[0], int2[0]), max(int1[1], int2[1]))
            return overlap, merged
        
        intervals.sort()
        print(intervals)
        out = [intervals[0]]
        
        for interval in intervals[1:]:
            overlap, merged = isoverlap(out[-1], interval)
            if overlap:
                out[-1] = merged
            else:
                out.append(interval)
        return out
            
