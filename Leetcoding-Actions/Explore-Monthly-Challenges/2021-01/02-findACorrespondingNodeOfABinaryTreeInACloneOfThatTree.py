# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        '''
        T: O(n) and S: O(n)
        '''
        qOriginal, qCloned = deque(), deque()
        qOriginal.append(original)
        qCloned.append(cloned)
        
        while qOriginal:
            currOriginal = qOriginal.popleft()
            currCloned = qCloned.popleft()
            if currOriginal == target:
                return currCloned
            if currOriginal.left: qOriginal.append(currOriginal.left)
            if currOriginal.right: qOriginal.append(currOriginal.right)
            if currCloned.left: qCloned.append(currCloned.left)
            if currCloned.right: qCloned.append(currCloned.right)
            
            
