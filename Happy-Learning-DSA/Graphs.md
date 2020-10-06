### Graph representation
* Adjacency matrix
* Adjacency list
  * Example graph representation with adjacency list
```
n = 4 # of nodes with ids: 0,1,2,3
edges = [[0,1], [0,2], [1,2], [2,0], [2,3]]

def buildGraph(edges):
    adj = collections.defaultdict(list)
    for edge in edges:
        adj[edge[0]].append(edge[1])
    return adj
```
### Graph traversal
* BFS
```
def bfs(graph, startNode):
    q = collections.deque()
    q.append(startNode)
    
    visited = set()
    visited.add(startNode)
    
    nodes = []
    
    while q:
        currNode = q.popleft()
        nodes.append(currNode)
        for neighbor in graph[currNode]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return nodes

adj = buildGraph(edges)
print(bfs(adj, 0))
```

* DFS
```
def dfs(graph, startNode):
    q = []
    q.append(startNode)
    
    visited = set()
    visited.add(startNode)
    
    nodes = []
    
    while q:
        currNode = q.pop()
        nodes.append(currNode)
        for neighbor in graph[currNode]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    return nodes

adj = buildGraph(edges)
print(dfs(adj, 0))
```

### Minimum Spanning Tree
* Spanning tree is generated from a weighted graph G(V, E). The graph could be directed or undirected.
* Spanning tree: Generated from a graph excluding cycles. The generated graph (essentially a tree) contains the following properties:
  * Number of vertices in spanning tree, V’ = V
  * Number of edges in spanning tree, E’ = V - 1
  * Number of possible spanning tree = E_C_(V-1) - number of cycles in graph
* MST is a spanning tree that gives minimum cost (sum of edges’ weights). So, it’s a optimization problem, which can be solved using greedy methods. Two widely used algorithms are:
  * Prim’s algorithm:
    * Start with minimum cost edge
    * Continue with the next minimum cost edge connected to already considered vertices
    * Stop when the number of edges is equal to V - 1

  * Krushkals algorithm
    * Start with the minimum cost edge
    * Continue with the next minimum cost edge, but skip if that forms any loop
    * Stop when the number of edges is equal to V - 1
    * Time complexity: Find the minimum from E edge costs for (V-1) times, so O(E.(V-1)) = O(n^2), which can be improved to O(n log n) by using min heap.

### Shortest path algorithms
* Dijkstra algorithm:
  * Step 1: Assign gain 0 to source node and gain infinity to all other nodes
  * Step 2: Start from the source node (visiting node), i.e., node with the minimum gain
  * Step 3: Relax the nodes connected to the visiting node.
	    * Relaxation: from visiting node u to its connected node v
     ```
	    if gain[u] + cost(u,v) < gain[v]:
		       gain[v] = gain[u] + cost(u, v)
     ```
  * Step 4: Select the node with minimum gain from remaining nodes, i.e., from the nodes that have not been considered as visiting node yet, and repeat step 3. Continue until each node is considered as the visiting node.
  * Time complexity: We visit all vertices and at each visiting node we relax all its connected node, so O(V.V) = O(n^2)
  * Example:
```
    2       7       1
.——————>2——————>4———————.
|       |       ^       |
|       |       |       v
1       |1      |2      6
|       |       |       ^
|       v       |       |
.——————>3——————>5———————.
   4        3       5
```
