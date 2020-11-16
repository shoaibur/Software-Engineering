
def findJudge(self, N: int, trust: List[List[int]]) -> int:

    trust = {tuple(pair): True for pair in trust}
    def trusts(a, b):
        return (a,b) in trust
    
    judge = 1
    for i in range(2, N+1):
        if trusts(judge, i):
            judge = i
    # Check judge trusts nobody
    for i in range(1, judge):
        if trusts(judge, i):
            return -1
    # Check everybody trusts judge
    for i in range(1, N+1):
        if i == judge: continue
        if not trusts(i, judge):
            return -1

    return judge
