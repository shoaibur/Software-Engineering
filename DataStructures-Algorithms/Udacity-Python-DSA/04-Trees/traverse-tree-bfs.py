def bfs(tree):
    # Queue
    q = []
    
    # Push in queue
    q.insert(0, tree)
    
    out = []
    
    while len(q) > 0:
        # deq
        node = q.pop()
        
        # visit
        print(node.value)
        out.append(node.value)
        
        # enq left
        if node.left:
            q.insert(0, node.left)
        
        # enq right
        if node.right:
            q.insert(0, node.right)
    return out
