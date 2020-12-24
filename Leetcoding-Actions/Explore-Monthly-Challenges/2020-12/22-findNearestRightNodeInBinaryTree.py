# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        '''
        T: O(n) and S: O(1)
        '''
        q = deque()
        q.append(root)
        
        while q:
            size = len(q)
            count = 0
            foundNode = False
            while count < size:
                curr = q.popleft()
                if foundNode:
                    return curr
                if curr == u:
                    foundNode = True
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                count += 1
        return None
