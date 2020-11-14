class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        for course in range(numCourses):
            adj[course] = []
        for course in prerequisites:
            adj[course[0]].append(course[1])
        
        visited = [0] * numCourses
        visiting = [0] * numCourses
        result = []
        
        def dfs(node):
            if visiting[node]: return True
            if visited[node]: return False
            visiting[node] = 1
            for neighbor in adj[node]:
                if dfs(neighbor):
                    return True
            visiting[node] = False
            visited[node] = True
            result.append(node)
            return False
        
        for node in range(numCourses):
            if dfs(node):
                return []
        return result
    
