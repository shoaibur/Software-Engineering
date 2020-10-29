class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        T: O(n log n) and S: O(n)
        '''
        if not intervals: return 0
        
        start = sorted([interval[0] for interval in intervals])
        end = sorted([interval[1] for interval in intervals])
        
        rooms = 0
        i, j = 0, 0
        while i < len(start):
            if start[i] < end[j]:
                rooms += 1
            else:
                j += 1
            i += 1
        
        return rooms
