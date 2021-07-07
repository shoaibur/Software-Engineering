class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        '''
        T: O(n) and S: O(n)
        '''
        n = len(popped)
        
        i = 0
        stack = []
        
        for item in pushed:
            stack.append(item)
            while stack and i < n and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        
        return i == n
