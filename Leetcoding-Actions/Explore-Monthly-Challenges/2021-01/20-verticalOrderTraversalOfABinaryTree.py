# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        q = collections.deque()
        q.append((root, 0, 0))
        
        nodes = {}
        while q:
            node, i, j = q.popleft()
            if i in nodes:
                nodes[i].append([j, node.val])
            else:
                nodes[i] = [[j, node.val]]
            
            if node.left: q.append((node.left, i-1, j-1))
            if node.right: q.append((node.right, i+1, j-1))

        minCol = min(list(nodes.keys()))
        maxCol = max(list(nodes.keys()))
        
        result = []
        for col in range(minCol, maxCol+1):
            temp = sorted(nodes[col], key=lambda x: (-x[0],x[1]))
            temp = [item[1] for item in temp]
            result.append(temp)
        return result
