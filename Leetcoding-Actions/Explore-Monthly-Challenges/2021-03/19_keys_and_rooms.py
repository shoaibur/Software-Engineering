class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        T: O(n) and S: O(n)
        '''
        visited = [False] * len(rooms)
        visited[0] = True
        stack = [0]
        
        while stack:
            curr = stack.pop()
            for room in rooms[curr]:
                if not visited[room]:
                    visited[room] = True
                    stack.append(room)
        
        return all(visited)
