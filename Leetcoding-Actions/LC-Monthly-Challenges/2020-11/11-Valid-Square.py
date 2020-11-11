class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        '''
        p1(x1, y1)      p3(x2, y1)
        -----------------
        |               |
        |               |
        |               |
        |               |
        |               |
        -----------------
        p2(x1, y2)      p4(x2, y2)
        
        x1 < x2 and y2 < y1
        First sort by ascending x that will put p1 and p2 in first two positions.
        Then sort by descending y that will put p3 and p4 in the next two positions.
        
        If all arm are equal in length and diagonals are equal in length,
        then four points will make a valid square.
        
        T: O(1) and S:O(1)
        '''
        def dist(p1, p2):
            return math.sqrt((p1[0]-p2[0]) ** 2 + (p1[1]-p2[1]) ** 2)
        
        p = [p1, p2, p3, p4]
        p.sort(key = lambda x: (x[0], -x[1]))
        p1, p2, p3, p4 = p
        
        # Arms
        d12 = dist(p1, p2)
        d24 = dist(p2, p4)
        d43 = dist(p4, p3)
        d31 = dist(p3, p1)
        # Diagonals
        d14 = dist(p1, p4)
        d23 = dist(p2, p3)
        
        # Check if any arms or diagonals are zero.
        if d14 == 0 or d23 == 0:
            return False
        
        return d12 == d24 and d24 == d43 and d43 == d31 and d14 == d23
