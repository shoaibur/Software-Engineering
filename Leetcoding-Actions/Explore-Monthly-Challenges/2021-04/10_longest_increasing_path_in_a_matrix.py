class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        visited = dict()
        def dfs(i, j):
            sublength = 1
            path_length = 0
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x <= len(matrix) - 1 and 0 <= y <= len(matrix[0]) - 1 and matrix[i][j] < matrix[x][y]:
                    if (x, y) in visited:
                        path_length = max(path_length, visited[(x, y)])
                    else:
                        path_length = max(path_length, dfs(x, y))

            visited[(i, j)] = path_length + sublength
            return path_length + sublength
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) not in visited:
                    dfs(i, j)
        
        return max(visited.values())
