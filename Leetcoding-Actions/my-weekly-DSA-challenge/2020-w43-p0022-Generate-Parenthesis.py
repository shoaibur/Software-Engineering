class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
            (
            /\
           (  )
           /\ /\
          (  )( )
        T: O(4^n / sqrt(n)) and S: O(4^n / sqrt(n))
        '''
        result = []
        
        def generate(s, nopen, nclose):
            if len(s) == 2*n:
                result.append(s)
            if nopen < n:
                generate(s + '(', nopen + 1, nclose)
            if nclose < nopen:
                generate(s + ')', nopen, nclose + 1)
                
        generate('', 0, 0)
        return result
