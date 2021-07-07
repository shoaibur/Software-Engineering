class Solution:
    def isValid(self, s: str) -> bool:
        '''
        T: O(n) and S: O(n)
        '''
        n = len(s)
        if n % 2: return False
        
        maps = {'(':')', '{':'}', '[':']'}
        
        stack = []
        for p in s:
            if p in '({[':
                stack.append(p)
            else:
                if not stack: return False
                else:
                    openP = stack.pop()
                    if maps[openP] != p:
                        return False
                    
        return len(stack) == 0
