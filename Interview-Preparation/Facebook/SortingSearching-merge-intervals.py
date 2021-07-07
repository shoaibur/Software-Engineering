class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals: return []
        
        def isoverlap(i1, i2):
            overlap = False
            merged = 'NA'
            if i1[1] >= i2[0]:
                overlap = True
            if overlap:
                merged = [min(i1[0], i2[0]), max(i1[1], i2[1])]
            return overlap, merged
        
        intervals.sort()
        print(intervals)
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            i1 = result[-1]
            i2 = intervals[i]
            overlap, merged = isoverlap(i1, i2)
            if overlap:
                result[-1] = merged
            else:
                result.append(i2)
        return result
