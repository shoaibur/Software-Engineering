class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                stack.append(0)
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()
