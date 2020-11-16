class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        if len(s) % 2: return False
        if s[0] in ']})': return False
        
        maps = {'(':')', '{':'}', '[':']'}
        
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack: return False
                else:
                    temp = stack.pop()
                    if maps[temp] != char:
                        return False
        return len(stack) == 0
