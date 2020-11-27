"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        T: O(V + E) = O(n) and S: O(n)
        '''
        if not node: return None
        
        clone = {}
        clone[node] = Node(node.val)
                
        q = deque()
        q.append(node)
        
        while q:
            curNode = q.popleft()
            for neighbor in curNode.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                clone[curNode].neighbors.append(clone[neighbor])
        
        return clone[node]
