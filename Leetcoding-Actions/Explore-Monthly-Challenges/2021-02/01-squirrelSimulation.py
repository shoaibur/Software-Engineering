class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        
        def distance(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        
        maxs = 0
        totalDist = 0
        for nut in nuts:
            nut2tree = distance(tree, nut)
            totalDist += 2 * nut2tree
            
            nut2squireel = distance(nut, squirrel)
            
            if nut2tree - nut2squireel > maxs:
                maxs = nut2tree - nut2squireel
        
        return totalDist - maxs if maxs else totalDist + abs(nut2tree-nut2squireel)
