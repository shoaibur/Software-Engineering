"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        # set that contains all the child nodes.
        seen = set()

        # add all the child nodes into the set
        for node in tree:
            for child in node.children:
                # we could either add the value or the node itself.
                seen.add(child.val)

        # find the node that is not in the child node set.
        for node in tree:
            if node.val not in seen:
                return node
