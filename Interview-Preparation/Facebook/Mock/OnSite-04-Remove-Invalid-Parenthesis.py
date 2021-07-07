class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:        
        if not s: return ['']
        
        result = set()
        maxx = 0
        
        def dfs(s, tempResult, nOpen, maxOpen):
            nonlocal maxx
            
            # Base condition
            if len(s) == 0:
                if nOpen == 0 and len(tempResult) != 0:
                    maxx = max(maxx, maxOpen)
                    if maxOpen == maxx and tempResult not in result:
                        result.add(tempResult)
                # if nOpen == 0 and len(tempResult) != 0 and tempResult not in result:
                #     result.add(tempResult)
                return
            
            if s[0] == '(':
                dfs(s[1:], tempResult+'(', nOpen+1, maxOpen+1) # keep (
                dfs(s[1:], tempResult, nOpen, maxOpen) # drop (
            elif s[0] == ')':
                if nOpen > 0:
                    dfs(s[1:], tempResult+')', nOpen-1, maxOpen) # keep )
                dfs(s[1:], tempResult, nOpen, maxOpen) # drop )
            else:
                dfs(s[1:], tempResult+s[0], nOpen, maxOpen) # keep letter
        
        dfs(s, '', 0, 0)
        if len(result) == 0:
            result.add('')
        return result
