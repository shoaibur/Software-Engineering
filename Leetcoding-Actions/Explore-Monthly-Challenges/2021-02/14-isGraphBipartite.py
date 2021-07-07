class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph: return False
        
        colors = {}
        
        for i in range(len(graph)):
            if i not in colors and graph[i]:
                colors[i] = 1
                q = deque([i])
                while q:
                    u = q.popleft()
                    for v in graph[u]:
                        if v not in colors:
                            colors[v] = 1 - colors[u]
                            q.append(v)
                        if colors[u] == colors[v]:
                            return False
        return True
