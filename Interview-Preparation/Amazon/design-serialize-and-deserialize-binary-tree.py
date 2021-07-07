# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root, data=[]):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            data.append(None)
            return data
        else:
            data.append(root.val)
            self.serialize(root.left, data)
            self.serialize(root.right, data)
        return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] is None:
            data.pop(0)
            return None
        root = TreeNode(data[0])
        data.pop(0)
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
