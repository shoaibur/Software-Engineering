# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        
        path, paths = tuple(), list()
        
        def dfs(root, path, paths):
            path += tuple([root.val])
            if not root.left and not root.right:
                paths.append(path)
            if root.left: dfs(root.left, path, paths)
            if root.right: dfs(root.right, path, paths)
        dfs(root, path, paths)
        
        result = []
        for path in paths:
            tempPath = ''
            for i in range(len(path)):
                arrow = '' if i == len(path)-1 else '->'
                tempPath += str(path[i]) + arrow
            result.append(tempPath)
        return result
