class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        
        result = []
        
        q = collections.deque()
        q.append([0])
        
        while q:
            path = q.popleft()
            if path[-1] == n-1:
                result.append(path)
            else:
                visited = set()
                for node in graph[path[-1]]:
                    if node in visited:
                        break
                    visited.add(node)
                    q.append(path+[node])
        return result
