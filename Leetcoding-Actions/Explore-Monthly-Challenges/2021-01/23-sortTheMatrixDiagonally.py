class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        T: O(m * n * log(min(m, n))) and S: O(min(m, n))
        '''
        # hashmap to keep the diagonals
        hashmap = defaultdict(list)
        
        # fill the hashmap
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                heappush(hashmap[i - j], mat[i][j])

        # build output
        for i in range(m):
            for j in range(n):
                mat[i][j] = heappop(hashmap[i - j])
        
        return mat
