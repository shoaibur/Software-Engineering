class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        '''
        T: O(n) and S: O(n)
        '''
        visited = set()
        q = []
        q.append(start)
        
        while q:
            currIndex = q.pop()
            if arr[currIndex] == 0:
                return True
            
            leftIndex = currIndex - arr[currIndex]
            rightIndex = currIndex + arr[currIndex]
            
            if leftIndex >= 0 and leftIndex not in visited:
                visited.add(leftIndex)
                q.append(leftIndex)
            
            if rightIndex < len(arr) and rightIndex not in visited:
                visited.add(rightIndex)
                q.append(rightIndex)
        
        return False
