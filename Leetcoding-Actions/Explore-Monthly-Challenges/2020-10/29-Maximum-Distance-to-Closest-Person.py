class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        '''
        Solution 2: Using constant space.
        T: O(n) and S: O(1)
        '''
        n = len(seats)
        
        # Distance from left and right
        i, leftDist = 0, 0
        while seats[i] == 0:
            leftDist += 1
            i += 1
            
        j, rightDist = n - 1, 0
        while seats[j] == 0:
            rightDist += 1
            j -= 1
        
        maxDist = max(leftDist, rightDist)
        
        # Distance in middle positions
        zero = 0
        for k in range(i, j+1):
            if seats[k] == 0:
                zero += 1
            else:
                maxDist = max(maxDist, (zero + 1) // 2)
                zero = 0
        
        return maxDist
        
        
        '''
        # Solution 1: Using linear space
        # T: O(n) and S: O(n)
        
        people = [i for i,s in enumerate(seats) if s == 1]
        
        leftDist = people[0] - 0
        rightDist = len(seats) - 1 - people[-1]
        maxDist = max(leftDist, rightDist)
        
        for i in range(1, len(people)):
            d = (people[i] - people[i - 1]) // 2
            maxDist = max(maxDist, d)
            
        return maxDist
        '''
