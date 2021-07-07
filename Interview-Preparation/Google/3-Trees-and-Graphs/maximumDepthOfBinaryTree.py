# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        def depth(root):
            if not root: return 0
            if not root.left:
                return depth(root.right) + 1
            if not root.right:
                return depth(root.left) + 1
            return max(depth(root.left), depth(root.right)) + 1
        return depth(root)
