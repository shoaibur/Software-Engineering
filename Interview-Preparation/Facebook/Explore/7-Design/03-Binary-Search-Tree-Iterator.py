# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.curr_index = 0
        self.data = []
        def inorder(root):
            if root:
                inorder(root.left)
                self.data.append(root.val)
                inorder(root.right)
        inorder(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            next_value = self.data[self.curr_index]
            self.curr_index += 1
            return next_value
        return -1
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.curr_index < len(self.data)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
