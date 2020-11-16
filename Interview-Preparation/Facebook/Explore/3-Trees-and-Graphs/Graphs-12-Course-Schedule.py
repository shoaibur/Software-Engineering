def findOrder(numCourses, prerequisites):
    adj = {}
    for course in range(numCourses):
        adj[course] = []
    for course in prerequisites:
        adj[course[0]].append(course[1])

    visited = [0] * numCourses
    visiting = [0] * numCourses
    result = [] # delete - can finish

    def dfs(node): # check if cycling dependency
        if visiting[node]: return True
        if visited[node]: return False
        visiting[node] = 1
        for neighbor in adj[node]:
            if dfs(neighbor):
                return True
        visiting[node] = False
        visited[node] = True
        result.append(node) # delete - can finish
        return False

    for node in range(numCourses):
        if dfs(node):
            return [] # False - can finish
    return result # True - can finish
