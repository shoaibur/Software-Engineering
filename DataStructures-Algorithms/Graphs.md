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
    * Start with any node
    * Continue with the next minimum cost edge connected to already considered nodes
    * Stop when the number of edges is equal to V - 1
    
    ```
    def primsMST(connections, N):
        #connections is a list: connections[i] = [node_x, node_y, cost] where x, y = 1, 2, ..., N
	
        graph = collections.defaultdict(list)
        for connection in connections:
            node1, node2, cost = connection
            graph[node1].append((node2,cost))
            graph[node2].append((node1,cost))
        
        visited = set()
        minCost = 0
        minHeap = [(0,1)] # start with node 1 and init cost 0
        while minHeap:
            node, cost = heapq.heappop(minHeap)
            if node not in visited: # Add node to the network
                visited.add(node)
                minCost += cost
            for neighbor, cost in graph[node]:
                if neighbor not in visited: # Add node to the heap
                    heapq.heappush(minHeap, (cost, neighbor))
        return minCost if len(visited) == N else -1
    ```
    
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
  * *Dijkstra result may or may not be correct if one or more weights are negatives.
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

Starting point: 1
-----------------
selected	2	3	4	5	6
---------------------------------------------------
1		2*	4	inf	inf	inf
2		2*	3*	9	inf	inf
3		2*	3*	9	6*	inf
5		2*	3*	8*	6*	10
4		2*	3*	8*	6*	9
```

* Bellman-Ford algorithm:
  * Step 0:
    * List all pairs of edges
    * Count number of the vertex = n
  * Step 1: Assign gain 0 to source node and gain infinity to all other nodes
  * Step 2: For each edge, relax nodes using the relaxation formula above
  * Step 3: Continue step 2 for (n-1) times
    * if gains of nodes do not change/update, stop before loop through all n-1 times.
  * Return distances/gains obtained in the last update.
  * *Bellman-Ford fails if there exists a loop with net negative weights.

* Floyd-Warshall algorithm:
  * Step 0: Count number of vertices = n
  * Step 1: Create an n x n matrix (A<sup>0</sup>)
    * Each row represents source nodes and each col represents destination nodes.
    * Fill out the matrix with distance values from source to destination.
    * Note that diagonals are zero (i.e., source and destination are same).
  * Step 2: Update matrix to A<sup>1</sup>, A<sup>2</sup>, ..., A<sup>n</sup>. To compute A<sup>k</sup>:
    * Don't change values for row/col for kth node, i.e., use same values from A<sup>k-1</sup>
    * Keep diagonals 0
    * Update other elements using the following formula:
      * A<sup>k</sup>[i, j] = min { A<sup>k-1</sup>[i, j], A<sup>k-1</sup>[i, k] + A<sup>k-1</sup>[j, k] }
  * Return pairwise distances represented in A<sup>n</sup>

### Topological sorting
* Graph must be Directed and Acyclic Graph (DAG)
* Topological sorting is a linear order such that u comes before v for each [u, v]
  * For each node, run a DFS in which
    * Maintain a visited set, and add the current node to the visited set.
    * For each neighbor of the current node, call DFS recursively.
