class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        '''
        T: O(n)
        S: O(1)
        '''
        sumTotal = sum(A)
        sumEachPart = sumTotal / 3
        if sumEachPart % 1 != 0: return False
        
        # Find each part that sums equal to sumEachPart
        countParts = 0
        curSum = 0
        for i, num in enumerate(A):
            curSum += num
            if curSum == sumEachPart:
                countParts += 1
                curSum = 0 # Start over for the next part
                if countParts > 3: return False
        return countParts == 3
