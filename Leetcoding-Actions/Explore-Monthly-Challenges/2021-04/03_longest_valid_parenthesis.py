class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        maxLen = 0
        stack = [-1]
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i - stack[-1])
        return maxLen
