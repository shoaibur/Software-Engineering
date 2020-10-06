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
