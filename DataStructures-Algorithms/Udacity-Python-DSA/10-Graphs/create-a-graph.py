class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = None
    def add_child(self, node):
        self.children.append(node)
#         

class Graph(object):
    def __init__(self, nodes):
        self.nodes = nodes
    def add_edges(self, node1, node2):
        if node1 in self.nodes and node2 in self.nodes:
            node1.add_child(node2)
            node2.add_child(node1)
#         

nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodes = [nodeA, nodeB, nodeC]
graph = Graph(nodes)
graph.add_edges(nodeA, nodeB)
graph.add_edges(nodeA, nodeC)
