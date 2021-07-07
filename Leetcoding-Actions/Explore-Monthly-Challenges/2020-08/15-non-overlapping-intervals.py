class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        count = 0
        if not intervals: return count
        intervals.sort()
        prevEnd = intervals[0][1]
        for interval in intervals[1:]:
            if prevEnd > interval[0]:
                count += 1
                prevEnd = min(prevEnd, interval[1])
            else:
                prevEnd = interval[1]
        return count
        
        
        # count = 0
        # if not intervals:
        #     return count
        # intervals.sort()
        # i1 = intervals[0]
        # for i2 in intervals[1:]:
        #     if i1[1] > i2[0]:
        #         count += 1
        #     else:
        #         i1 = i2
        # return count
            
