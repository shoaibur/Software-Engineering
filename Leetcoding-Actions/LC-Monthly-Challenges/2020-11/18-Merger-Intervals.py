class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        T: O(n log n) and S: O(1)
        '''
        intervals.sort()
        
        result = []
        
        result.append(intervals[0]);
        
        for i in range(1, len(intervals)):
            i1 = result[-1]
            i2 = intervals[i]
            
            if i1[1] >= i2[0]:
                merged = [min(i1[0], i2[0]), max(i1[1], i2[1])];
                result[-1] = merged
            else:
                result.append(i2)
        return result
