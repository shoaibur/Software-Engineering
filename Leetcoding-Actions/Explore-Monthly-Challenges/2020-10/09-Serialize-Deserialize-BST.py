# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root: return ''
        data = []
        q = deque()
        q.append(root)
        while q:
            curr = q.popleft()
            if curr:
                data.append(str(curr.val))
                q.append(curr.left)
                q.append(curr.right)
            else:
                data.append('#')
        return ','.join(data)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if not data: return None
        data = deque(data.split(','))
        
        val = data.popleft()
        root = TreeNode(val)
        
        q = deque()
        q.append(root)
        
        while q:
            curr = q.popleft()
            
            left = data.popleft()
            if left != '#':
                curr.left = TreeNode(int(left))
                q.append(curr.left)
            
            right = data.popleft()
            if right != '#':
                curr.right = TreeNode(int(right))
                q.append(curr.right)
        
        return root

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans




# Serialize and deserialize binary tree
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return []
        
        data = []
        q = deque()
        q.append(root)
        
        while q:
            curr = q.popleft()
            
            if curr:
                data.append(curr.val)
                q.append(curr.left)
                q.append(curr.right)
            else:
                data.append(None)
        return data

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        
        data = deque(data)
        
        val = data.popleft()
        root = TreeNode(val)
        
        q = deque()
        q.append(root)
        
        while q:
            curr = q.popleft()
            
            left = data.popleft()
            if left is not None:
                curr.left = TreeNode(left)
                q.append(curr.left)
            
            right = data.popleft()
            if right is not None:
                curr.right = TreeNode(right)
                q.append(curr.right)
        
        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
