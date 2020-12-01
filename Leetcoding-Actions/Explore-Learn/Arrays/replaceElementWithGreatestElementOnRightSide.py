class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        T: O(n) and S: O(1)
        '''
        currMax = -1
        for i in range(len(arr) - 1, -1, -1):
            currVal = arr[i]
            arr[i] = currMax
            currMax = max(currMax, currVal)
        return arr
