class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        [[0, 30],[5, 10],[15, 20]]
        start = [0, 5, 15]
        end = [10, 20, 30]
        
        T: O(n log n) and S: O(n log n)
        '''
        
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
