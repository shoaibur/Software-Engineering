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
