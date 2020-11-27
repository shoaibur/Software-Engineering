# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        path, paths = tuple(), list()
        
        def getPath(root, path, paths):
            if not root: return
            path += tuple([root.val])
            if not root.left and not root.right:
                paths.append(path)
            if root.left: getPath(root.left, path, paths)
            if root.right: getPath(root.right, path, paths)
            
        getPath(root, path, paths)
        result = 0
        for path in paths:
            pathNum = 0
            for i in range(len(path)-1, -1, -1):
                pathNum += path[i] * 2 ** (len(path)-1-i)
            result += pathNum
        return result
