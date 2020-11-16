class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parenthesis = []
        if n == 0: return parenthesis
        
        def generate(s = '', nopen = 0, nclose = 0):
            if len(s) == 2 * n:
                parenthesis.append(s)
                return parenthesis
            if nopen < n:
                generate(s + '(', nopen + 1, nclose)
            if nclose < nopen:
                generate(s + ')', nopen, nclose + 1)
        
        generate()
        return parenthesis
