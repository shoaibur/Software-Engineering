# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        Solution 3:
        T: O(n) and S: O(H)
        n = number of nodes in the tree
        H = height of the tree
        '''
        stack = []
        currNode = root
        # nodes = []
        first, second, prev = None, None, TreeNode(float('-inf'))
        
        while True:
            while currNode:
                stack.append(currNode)
                currNode = currNode.left
                
            if not stack: break
            currNode = stack.pop()
            # nodes.append(currNode.val)
            if currNode.val < prev.val:
                second = currNode
                if not first:
                    first = prev
                else: break
            prev = currNode
            currNode = currNode.right
        
        first.val, second.val = second.val, first.val

        
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        Solution 2:
        T: O(n) and S: O(n)
        n = number of nodes in the tree
        '''
        nodes = []
        def inorder(root):
            if root:
                inorder(root.left)
                nodes.append(root)
                inorder(root.right)
        inorder(root)
        
        first, second = None, None
        for i in range(1, len(nodes)):
            if nodes[i-1].val > nodes[i].val:
                second = (i, nodes[i].val)
                if not first:
                    first = (i-1, nodes[i-1].val)
                else:
                    break
        
        nodes[first[0]].val = second[1]
        nodes[second[0]].val = first[1]
        
        return root

    
    
    
    
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        Solution 1:
        T: O(n) and S: O(n)
        n = number of nodes in the tree
        '''
        nodes = []
        def inorder(root):
            if root:
                inorder(root.left)
                nodes.append(root)
                inorder(root.right)
        inorder(root)
        
        # First swap node: Traverse from left, take the first one bigger than its next right
        for i in range(1, len(nodes)):
            if nodes[i-1].val > nodes[i].val:
                first = (i-1, nodes[i-1].val)
                break
        # Second swap node: Traverse from right, take the first one smaller than its next left
        for i in range(len(nodes)-2, -1, -1):
            if nodes[i+1].val < nodes[i].val:
                second = (i+1, nodes[i+1].val)
                break
        
        nodes[first[0]].val = second[1]
        nodes[second[0]].val = first[1]
        
        return root
