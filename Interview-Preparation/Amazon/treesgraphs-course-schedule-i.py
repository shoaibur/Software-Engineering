class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for course in range(numCourses):
            adj[course] = []
        for pairs in prerequisites:
            adj[pairs[0]].append(pairs[1])
        
        visiting = [0] * numCourses
        visited = [0] * numCourses
        
        def dfs(node):
            if visiting[node]: return True
            if visited[node]: return False
            
            visiting[node] = 1
            for neighbor in adj[node]:
                if dfs(neighbor): return True
            visiting[node] = 0
            visited[node] = 1
            
            return False
        
        
        for node in range(numCourses):
            if dfs(node): return False
        return True
        
