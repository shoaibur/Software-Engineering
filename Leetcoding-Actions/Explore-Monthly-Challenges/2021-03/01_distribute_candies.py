class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        n = len(candyType)
        
        d = {}
        for candy in candyType:
            d[candy] = d.get(candy, 0) + 1
        
        return len(d) if len(d) <= n // 2 else n // 2
    
