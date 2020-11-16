def accountsMerge(accounts):
    # Build adj list O(n = #accounts)
    email2name = {}
    adjList = collections.defaultdict(set)
    for acc in accounts:
        for email in acc[1:]:
            adjList[email].add(acc[1])
            adjList[acc[1]].add(email)
            email2name[email] = acc[0]
    # DFS to gather connected components O(nlog(n))
    result = []
    visited = set()
    for email in adjList:
        if email in visited: continue
        visited.add(email)
        stack = [email]
        emails = []
        while stack:
            currEmail = stack.pop()
            emails.append(currEmail)
            for altEmail in adjList[currEmail]:
                if altEmail in visited: continue
                visited.add(altEmail)
                stack.append(altEmail)
        result.append([email2name[email]] + sorted(emails))
    return result
