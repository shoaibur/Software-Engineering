class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == ')': return False
        
        openClose = {'(':')', '{':'}', '[':']'}
        
        stack = []
        for i in range(len(s)):
            if s[i] in '({[':
                stack.append(s[i])
            else:
                if not stack: return False
                opens = stack.pop()
                if s[i] != openClose[opens]: return False
        return len(stack) == 0
