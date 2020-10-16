class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        T: O(m * n)
        S: O(1)
        '''
        result = []
        turn = 0
        while len(matrix) > 0 and len(matrix[0]) > 0:
            if turn % 4 == 0:
                result.extend(matrix.pop(0))
            elif turn % 4 == 1:
                for i in range(len(matrix)):
                    result.append(matrix[i].pop())
            elif turn % 4 == 2:
                result.extend(matrix.pop()[::-1])
            else:
                for i in range(len(matrix)-1, -1, -1):
                    result.append(matrix[i].pop(0))
            turn += 1
        return result
