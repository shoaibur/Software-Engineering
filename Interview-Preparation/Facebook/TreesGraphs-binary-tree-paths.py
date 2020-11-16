# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # paths = []
        # if not root: return paths
        # def dfs(root, path, paths):
        #     path += str(root.val)
        #     if not root.left and not root.right:
        #         paths.append(path)
        #         return
        #     if root.left:
        #         dfs(root.left, path+'->', paths)
        #     if root.right:
        #         dfs(root.right, path+'->', paths)
        # dfs(root, '', paths)
        # return paths
        
        path = []
        if not root: return path
        
        def inorder(root):
            if not root: return
            path.append(root.val)
            
            inorder(root.left)
            if not root.left and not root.right:
                print(path)
                # paths.append(path)
            inorder(root.right)
            
            path.pop()
        
        inorder(root)
