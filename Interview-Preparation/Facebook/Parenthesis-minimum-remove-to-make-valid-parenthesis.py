class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        invalid = {}
        stack = []
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append((char, i))
            elif char == ')':
                if not stack:
                    invalid[i] = i
                else:
                    stack.pop()
        
        for item in stack:
            invalid[item[1]] = item[1]
        
        return ''.join([s[i] for i in range(len(s)) if i not in invalid])
