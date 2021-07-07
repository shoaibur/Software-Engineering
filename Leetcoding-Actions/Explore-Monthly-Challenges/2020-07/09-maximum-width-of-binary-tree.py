# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        if root is None: return 0
        
        q = collections.deque()
        root_idx = 0
        q.append((root, root_idx))
        
        max_width = 0
        while len(q) > 0:
            size = len(q)
            max_width = max(max_width, q[-1][1] - q[0][1] + 1)
            count_level = 0
            while count_level < size:
                pop = q.popleft()
                
                if pop[0].left:
                    left_idx = 2 * pop[1] + 1
                    q.append((pop[0].left, left_idx))
                if pop[0].right:
                    right_idx = 2 * pop[1] + 2
                    q.append((pop[0].right, right_idx))
                count_level += 1
                
        return max_width
