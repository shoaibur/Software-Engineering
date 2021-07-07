# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        stack, res = [root], []
        for i in range(len(voyage) - 1):
            node = stack.pop()
            if node.val != voyage[i]:
                return [-1]
            if node.left and node.right and node.right.val == voyage[i + 1]:
                res.append(node.val)
                stack.extend([node.left, node.right])
            else:
                stack.extend(child for child in [node.right, node.left] if child)
        return res
