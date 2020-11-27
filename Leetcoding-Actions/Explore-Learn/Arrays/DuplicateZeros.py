class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        T: O(n) and S: O(n)
        """
        # Position of first 0
        for i in range(len(arr)):
            if arr[i] == 0: break
        
        # Zero positions and nonZero elements
        zeroPosition = set()
        nonZeroQ = deque()
        zerosCount = 0
        for j in range(i, len(arr)):
            if arr[j] == 0:
                zerosCount += 1
                zeroPosition.add(j + zerosCount - 1)
                zeroPosition.add(j + zerosCount - 1 +1)
            else:
                nonZeroQ.append(arr[j])
        
        # Put 0 at zeroPosition and put nonZero elements at other position 
        for j in range(i, len(arr)):
            if j in zeroPosition:
                arr[j] = 0
            else:
                arr[j] = nonZeroQ.popleft()
