# Helper classes
class Edge:
    def __init__(self, node, distance=1):
        self.node = node
        self.distance = distance
        
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        
    def add_child(self, node, distance=1):
        self.children.append(Edge(node, distance))
        
class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        
    def add_edge(self, node1, node2, distance=1):
        node1.add_child(node2, distance)
        node2.add_child(node1, distance)
        
# Create a graph        
nodeA = Node('A')
nodeB = Node('B')
nodeC = Node('C')
nodeD = Node('D')

graph = Graph([nodeA, nodeB, nodeC, nodeD])
graph.add_edge(nodeA, nodeB, distance=1)
graph.add_edge(nodeA, nodeC, distance=2)
graph.add_edge(nodeC, nodeD, distance=2)
graph.add_edge(nodeB, nodeD, distance=4)
graph.add_edge(nodeB, nodeC, distance=5)

# Shortest path algorithm - dijkstra algorithm
import math   # Need math.inf constant
def dijkstra(graph, start_node, end_node):
    # Create a dictionary that stores the distance to all nodes in the form of node:distance as key:value 
    # Assume the initial distance to all nodes is infinity.
    # Use math.inf as a predefined constant equal to positive infinity 
    distance_dict = {node: math.inf for node in graph.nodes} # O(V)
    distance_dict[start_node] = 0
    
    # Build a dictionary that will store the "shortest" distance to all nodes, wrt the start_node
    shortest_distance = {}
    
    while distance_dict: # O(V)
        
        # Sort the distance_dict, and pick the key:value having smallest distance
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0] # O(V log V)
        
        # Remove the current node from the distance_dict, and store the same key:value in shortest_distance
        shortest_distance[current_node] = distance_dict.pop(current_node)

        # Check for each neighbour of current_node, if the distance_to_neighbour is smaller than the 
        # alreday stored distance, update the distance_dict.
        for child in current_node.children: # O(E)
            if child.node in distance_dict:
                
                distance_to_neighbour = node_distance + child.distance
                if distance_dict[child.node] > distance_to_neighbour:
                    distance_dict[child.node] = distance_to_neighbour
    
    return shortest_distance[end_node]

# Runtime: O( V * (V log(V) + E) )
# Space: O(V)

# Test
print(f'Shortest distance between A and D is {dijkstra(graph, nodeA, nodeD)}')
# Shortest distance between A and D is 4
