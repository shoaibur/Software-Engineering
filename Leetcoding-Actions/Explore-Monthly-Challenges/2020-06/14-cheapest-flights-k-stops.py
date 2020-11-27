# There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
# Now given all the cities and flights, together with starting city src and the destination dst, your task 
# is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

def find_cheapest_price(n, flights, src, dst, K):
    adj = {u: [] for u in range(n)}
    for flight in flights:
        adj[flight[0]].append( (flight[1],flight[2]) )
    pq = []
    pq.append((0, src, K+1))
    while len(pq) > 0:
        d, u, e = heapq.heappop(pq)
        if dst == u: return d
        if e > 0:
            for v in adj[u]:
                heapq.heappush(pq, (d+v[1], v[0], e-1) )
    return -1
