# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        '''
        T: O(n) and S: O(n)
        '''
        if not root: return 0
        
        sum = 0
        stack = []
        curr = root
        
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            if not stack: break
                
            curr = stack.pop()
            
            if curr.val >= low and curr.val <= high:
                sum += curr.val
            if curr.val > high: return sum
            
            curr = curr.right
            
        return sum
