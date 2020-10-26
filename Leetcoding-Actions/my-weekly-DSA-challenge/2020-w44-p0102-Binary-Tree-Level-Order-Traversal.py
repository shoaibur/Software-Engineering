# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        '''
        T: O(n) and S: O(n)
        '''
        if not root: return []
        result = []
        q = deque()
        q.append(root)
        
        while q:
            level_size = len(q)
            level_node_count = 0
            level_nodes = []
            while level_node_count < level_size:
                curNode = q.popleft()
                level_nodes.append(curNode.val)
                if curNode.left: q.append(curNode.left)
                if curNode.right: q.append(curNode.right)
                level_node_count += 1
            result.append(level_nodes)
        return result
