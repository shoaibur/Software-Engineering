class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph: return False
        
        colors = {}
        
        for i in range(len(graph)):
            q = deque()
            if i not in colors and graph[i]:
                colors[i] = 1
                q.append(i)
                while q:
                    u = q.popleft()
                    for v in graph[u]:
                        if v not in colors:
                            colors[v] = 1 - colors[u]
                            q.append(v)
                        elif colors[v] == colors[u]:
                            return False
        return True
    
