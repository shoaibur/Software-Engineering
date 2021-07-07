class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegree = {}
        for char in string.ascii_lowercase:
            indegree[char] = 0
            
        graph = collections.defaultdict(set)
        for word in words:
            for char in word:
                if char not in graph:
                    graph[char]
        for i in range(1, len(words)):
            previous = words[i-1]
            current = words[i]
            length = min(len(previous), len(current))
            
            for j in range(length):
                outgoing = previous[j]
                incoming = current[j]
                if outgoing != incoming:
                    if incoming not in graph[outgoing]:
                        graph[outgoing].add(incoming)
                        indegree[incoming] += 1
                    break
                if j+1 == length and len(previous) > len(current):
                    return ''
        
        ans = ''
        q = collections.deque()
        for node in graph:
            if indegree[node] == 0:
                ans += node
                q.append(node)
        while len(q) > 0:
            node = q.popleft()
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    ans += neighbor
                    q.append(neighbor)
        return ans if len(ans) == len(graph) else ''
