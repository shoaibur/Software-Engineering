class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        '''
        T: O(n)
        S: O(1)
        '''
        minVal = arrays[0][0]
        maxVal = arrays[0][-1]
        maxDist = 0
        
        for array in arrays[1:]:
            dist_1 = abs(minVal - array[-1])
            dist_2 = abs(maxVal - array[0])
            maxDist = max(maxDist, dist_1, dist_2)
            
            minVal = min(minVal, array[0])
            maxVal = max(maxVal, array[-1])
        
        return maxDist
        
        
        ''' Solution 2
        [[1,2,3],
        [4,5],
        [1,2,3]]
        
        min = [1, 4, 1]
        max = [3, 5, 3]
        
        arrays --> m rows * n cols
        Time: O(m) + O(m^2) = O(m^2)
        Space: O(2m) = O(m)
        
        
        minVector = []
        maxVector = []
        for vector in arrays:
            minVector.append(vector[0])
            maxVector.append(vector[-1])
        
        maxDist = 0
        for i in range(len(minVector)):
            for j in range(len(maxVector)):
                if i == j: continue
                maxDist = max(maxDist, abs(minVector[i] - maxVector[j]))
        
        return maxDist
        '''
