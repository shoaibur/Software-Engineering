def alienOrder(self, words: List[str]) -> str:
    if not words: return ''
    allChars = set()
    orders = []
    w1 = words[0]
    for w2 in words[1:]:
        for i in range(min(len(w1), len(w2))):
            if w1[i] != w2[i]:
                orders.append([w1[i], w2[i]])
                allChars.add(w1[i])
                allChars.add(w2[i])
                # break
        w1 = w2

    adj = {}
    for char in allChars:
        adj[char] = []
    for order in orders:
        adj[order[0]].append(order[1])

    visiting = {char: False for char in allChars}
    visited = {char: False for char in allChars}
    result = []

    def dfs(node):
        if visiting[node]: return True
        if visited[node]: return False
        visiting[node] = True

        for neighbor in adj[node]:
            if dfs(neighbor): return True

        visiting[node] = False
        visited[node] = True
        result.append(node)
        return False

    for char in allChars:
        if dfs(char): return ''
    return ''.join(result[::-1])
