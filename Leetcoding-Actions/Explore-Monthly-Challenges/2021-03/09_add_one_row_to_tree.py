# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        '''
        T: O(n) and S: O(n)
        '''
        if d == 1:
            tree = TreeNode(v)
            tree.left = root
            return tree
    
        q = deque()
        q.append(root)
        
        temp = []
        level = 1
        while q:
            for node in q:
                if level == d - 1:
                    left, right = node.left, node.right
                    node.left, node.right = TreeNode(v), TreeNode(v)               
                    node.left.left, node.right.right = left, right
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            q = temp
            temp = []
            level += 1
            
        return root
