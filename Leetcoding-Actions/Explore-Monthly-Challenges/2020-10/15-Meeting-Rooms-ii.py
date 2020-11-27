class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        [[0, 30],[5, 10],[15, 20]]
        starts: 0 5 15
        ends: 10 20 30
        T: O(n log n)
        S: O(1)
        '''
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])
        
        roomsRequired = 0
        i, j = 0, 0
        while i < len(starts):
            if starts[i] < ends[j]:
                roomsRequired += 1
            else:
                j += 1
            i += 1
        
        return roomsRequired
