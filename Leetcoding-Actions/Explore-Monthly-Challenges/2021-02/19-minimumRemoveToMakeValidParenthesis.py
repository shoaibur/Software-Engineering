class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        invalid_open = []
        invalid_close = []
        
        for i,char in enumerate(s):
            if char == '(':
                invalid_open.append(i)
            elif char == ')':
                if not invalid_open:
                    invalid_close.append(i)
                else:
                    invalid_open.pop()
        invalid = invalid_open + invalid_close
        invalid = {i: True for i in invalid}
        
        return ''.join([s[i] for i in range(len(s)) if i not in invalid])
