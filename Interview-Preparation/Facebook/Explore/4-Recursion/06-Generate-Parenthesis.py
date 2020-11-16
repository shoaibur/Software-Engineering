class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        def generate(s, nopens, nclose):
            if len(s) == 2*n:
                result.append(s)
                return result
            if nopens < n:
                generate(s + '(', nopens + 1, nclose)
            if nclose < nopens:
                generate(s + ')', nopens, nclose + 1)
        generate('', 0, 0)
        return result
