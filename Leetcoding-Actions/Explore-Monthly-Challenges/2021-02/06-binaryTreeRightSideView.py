# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        
        q = deque()
        q.append(root)
        
        rightSide = []
        while q:
            levelSize = len(q)
            nodeCount = 0
            temp = []
            while nodeCount < levelSize:
                currNode = q.popleft()
                temp.append(currNode.val)
                if currNode.left: q.append(currNode.left)
                if currNode.right: q.append(currNode.right)
                nodeCount += 1
            rightSide.append(temp[-1])
        return rightSide
        
