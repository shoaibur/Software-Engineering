class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        '''
        T: O(n log n) and S: O(1)
        '''
        if not intervals: return True
        
        intervals.sort()
        
        i1 = intervals[0]
        for i2 in intervals[1:]:
            if i1[1] > i2[0]:
                return False
            else:
                i1 = i2
                
        return True
