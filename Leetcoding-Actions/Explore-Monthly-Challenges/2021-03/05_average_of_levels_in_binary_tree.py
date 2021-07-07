# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        '''
        T: O(n) and S: O(1)
        '''
        if not root:
            return []
        
        level_average = []
        q = deque()
        q.append(root)
        
        while q:
            node_count = 0
            level_size = len(q)
            level_sum = 0
            while node_count < level_size:
                curr = q.popleft()
                level_sum += curr.val
                
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
                
                node_count += 1
                
            level_average.append(level_sum / level_size)
        
        return level_average
