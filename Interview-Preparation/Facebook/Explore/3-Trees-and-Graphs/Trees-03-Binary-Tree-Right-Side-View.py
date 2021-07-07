# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return None
        
        # levels = []
        rightView = []
        
        q = deque()
        q.append(root)
        
        while q:
            levelSize = len(q)
            countSize = 0
            # temp = []
            while countSize < levelSize:
                node = q.popleft()                
                
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
                
                countSize += 1
                if countSize == levelSize:
                    rightView.append(node.val)

        return rightView
        
