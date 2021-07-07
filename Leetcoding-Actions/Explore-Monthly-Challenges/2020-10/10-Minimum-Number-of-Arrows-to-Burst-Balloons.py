class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        [[10,16],[2,8],[1,6],[7,12]]
        Sort by ending point and 
        check how many ballons are overlapped by the first one; 
        skip those and continue from the one that is not overlapped.
        
        T: O(n log n + n) = O(n log n)
        S: O(1)
        '''
        if len(points) <= 1: return len(points)
        points.sort(key = lambda x: x[1])
        
        arrows = 1
        end1 = points[0][1]
        i = 1
        while i < len(points):
            start2 = points[i][0]
            if end1 < start2:
                arrows += 1
                end1 = points[i][1]
            i += 1
        return arrows
