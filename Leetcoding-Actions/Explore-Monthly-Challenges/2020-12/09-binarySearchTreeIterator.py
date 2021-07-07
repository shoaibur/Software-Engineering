# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.data = []
        def inorder(root):
            if root:
                inorder(root.left)
                self.data.append(root.val)
                inorder(root.right)
        inorder(root)
        self.index = 0

    def next(self) -> int:
        if self.hasNext():
            val = self.data[self.index]
            self.index += 1
            return val
        

    def hasNext(self) -> bool:
        return self.index < len(self.data)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
