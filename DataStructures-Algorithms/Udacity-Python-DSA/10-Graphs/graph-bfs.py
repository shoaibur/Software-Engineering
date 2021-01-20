def bfs(root):
    visited = []
    
    # queue
    q = [root]
    
    while q:
        # pop
        node = q.pop(0)
        
        # visit
        visited.append(node)
        
        # queue childred
        for child in node.children:
            if child not in visited:
                q.append(child)
    return [node.value for node in visited]
