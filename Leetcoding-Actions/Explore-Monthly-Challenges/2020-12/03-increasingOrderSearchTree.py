# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        '''
        T: O(n) and S: O(n)
        '''
        
        # Iterative inorder
        nodes = []
        stack = []
        curr = root
        while True:
            while curr:
                stack.append(curr)
                curr = curr.left
            if not stack: break
            
            curr = stack.pop()
            nodes.append(curr)
            curr = curr.right
        
        '''
        # Recursive inorder
        nodes = []
        def inOrder(root):
            if root:
                inOrder(root.left)
                nodes.append(root)
                inOrder(root.right)
        inOrder(root)
        '''
        
        for i in range(len(nodes) - 1):
            nodes[i].right = nodes[i+1]
            nodes[i].left = None
        nodes[-1].left = None
        nodes[-1].right = None
        return nodes[0]
