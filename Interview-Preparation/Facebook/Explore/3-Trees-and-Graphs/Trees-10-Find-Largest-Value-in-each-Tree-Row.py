def largestValues(root):
    if not root: return []

    q = collections.deque()
    q.append(root)
    out = []
    while q:
        size = len(q)
        count = 0
        temp = []
        while size > count:
            p = q.popleft()
            temp.append(p.val)

            if p.left: q.append(p.left)
            if p.right: q.append(p.right)
            count += 1
        out.append(temp)

    result = [max(item) for item in out]
    return result
