# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        res = []
        q = deque()
        q.append(root)
        
        while len(q) > 0:
            size = len(q)
            count = 0
            temp = []
            while count < size:
                pop = q.popleft()
                temp.append(pop.val)
                count += 1
                if pop.left:
                    q.append(pop.left)
                if pop.right:
                    q.append(pop.right)
            res.append(temp)
        for i in range(len(res)):
            if i%2:
                res[i] = res[i][::-1]
        return res

    
    
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        
        level_nodes = []
        
        q = collections.deque()
        q.append((root, 0))
        
        while q:
            node, level = q.popleft()
            level_nodes.append((node.val, level))
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))
        
        out = [[]]
        curr_level = 0
        for item in level_nodes:
            node_val, level = item
            if level > curr_level:
                curr_level = level
                out.append([node_val])
            else:
                out[level].append(node_val)
        for i in range(len(out)):
            if i % 2:
                out[i] = out[i][::-1]
        return out
