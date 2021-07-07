class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        (0,0)
        (1,0), (0,1)
        (2,0), (1,1), (0,2)
        (2,1), (1,0)
        (2,2)
        
        T: O(m + n)
        S: O(1)
        '''
        if not matrix: return []
        result = []
        turn = 0
        nrow, ncol = len(matrix), len(matrix[0])
        for i in range(nrow):
            j = 0
            temp = []
            while i >= 0 and j <= ncol-1:
                temp.append(matrix[i][j])
                j += 1
                i -= 1
            if turn % 2:
                temp = temp[::-1]
            result.extend(temp)
            turn += 1
            
        for j in range(1, ncol):
            i = nrow-1
            temp = []
            while i >= 0 and j <= ncol-1:
                temp.append(matrix[i][j])
                i -= 1
                j += 1
            if turn % 2:
                temp = temp[::-1]
            result.extend(temp)
            turn += 1
            
        return result
