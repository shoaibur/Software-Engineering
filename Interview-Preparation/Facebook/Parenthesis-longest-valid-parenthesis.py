class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        maxLen = 0
        stack = [-1] # imagine first invalid close at -1
        for i,char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i) # next invalid close
                else:
                    maxLen = max(maxLen, i - stack[-1])
        return maxLen
