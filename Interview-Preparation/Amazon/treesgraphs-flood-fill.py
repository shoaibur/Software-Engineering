class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        if not image: return image
        
        nrow = len(image)
        ncol = len(image[0])
        
        color = image[sr][sc]
        if color == newColor: return image
        
        def dfs(image, i, j):
            if image[i][j] == color:
                image[i][j] = newColor
                if i > 0:
                    dfs(image, i-1, j)
                if i < nrow-1:
                    dfs(image, i+1, j)
                if j > 0:
                    dfs(image, i, j-1)
                if j < ncol-1:
                    dfs(image, i, j+1)
        dfs(image, sr, sc)
        return image
