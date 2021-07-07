class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n <= 1: return n
        
        start = sorted([item[0] for item in intervals])
        end = sorted([item[1] for item in intervals])
        
        rooms = 0
        i, j = 0, 0
        while i < n:
            if start[i] >= end[j]:
                j += 1
            else:
                rooms += 1
            i += 1
        return rooms
