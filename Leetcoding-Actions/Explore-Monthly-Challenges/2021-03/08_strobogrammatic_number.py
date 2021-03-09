class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        '''
        T: O(n) and S: O(1)
        '''
        maps = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        
        i, j = 0, len(num) - 1
        while i <= j:
            if num[i] not in maps or num[j] not in maps:
                return False
            if num[i] == maps[num[j]]:
                i, j = i + 1, j - 1
            else:
                return False
        return True
