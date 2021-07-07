class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        '''
        Idea: Move all even positioned chips to 0, i.e., count them and 
        all odd positioned chips to 1, i.e., count them; take min of two counts
        T: O(n) and S: O(1)
        '''
        zeroCost, oneCost = 0, 0
        for i in range(len(position)):
            if position[i] % 2:
                oneCost += 1
            else:
                zeroCost += 1
            
        return min(zeroCost, oneCost)
