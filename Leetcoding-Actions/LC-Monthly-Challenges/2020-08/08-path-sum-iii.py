# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def dfs(node: TreeNode, sums: List[int]) -> int:
            if not node:
                return 0
            sums = [s + node.val for s in sums] + [node.val]
            res = sums.count(sum)
            res += dfs(node.left, sums) if node.left else 0
            res += dfs(node.right, sums) if node.right else 0
            return res
        return dfs(root, [])
