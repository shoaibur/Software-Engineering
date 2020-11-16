class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s: return ['']
        
        result = set()
        maxx = 0
        
        def remove(s, tempRes, nOpen, maxOpen):
            nonlocal maxx
            # Base condition
            if not s:
                if len(tempRes) != 0 and nOpen == 0:
                    maxx = max(maxx, maxOpen)
                    if maxx == maxOpen and tempRes not in result:
                        result.add(tempRes)
                return result
            
            elif s[0] == '(':
                remove(s[1:], tempRes+'(', nOpen+1, maxOpen+1)
                remove(s[1:], tempRes, nOpen, maxOpen)
            
            elif s[0] == ')':
                if nOpen > 0:
                    remove(s[1:], tempRes+')', nOpen-1, maxOpen)
                remove(s[1:], tempRes, nOpen, maxOpen)
            
            else:
                remove(s[1:], tempRes+s[0], nOpen, maxOpen)
        remove(s, '', 0, 0)
        if not result: return ['']
        return result
