class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        '''
        Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
        '''
        intervals.sort(key=lambda x:(x[0], -x[1]))
        
        count = 1
        i1 = intervals[0]
        for i2 in intervals[1:]:
            if i2[0] >= i1[0] and i1[1] >= i2[1]:
                continue
            else:
                count += 1
                i1 = i2
        return count
