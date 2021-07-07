def dfs(root):
    visited = []
    
    # stack
    stack = []
    
    # push
    stack.append(root)
    
    # while stack
    while stack:
        # pop
        node = stack.pop()
      
        # visit
        visited.append(node)
        
        # push children
        for child in node.children:
            if child not in visited:
                stack.append(child)
    return [node.value for node in visited]
