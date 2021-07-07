class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        '''
        T: O(n) and S: O(n)
        '''
        numSet = set()
        for i in range(len(arr)):
            if 2 * arr[i] in numSet:
                return True
            else:
                numSet.add(arr[i])
        
        revNumSet = set()
        for i in range(len(arr)-1, -1, -1):
            if 2 * arr[i] in revNumSet:
                return True
            else:
                revNumSet.add(arr[i])
                
        return False
