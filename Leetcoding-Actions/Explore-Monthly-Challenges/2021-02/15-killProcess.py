class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        '''
        T: O(n) and S: O(n)
        '''
        # Adjacency list
        tree = collections.defaultdict(set)
        for p, c in zip(ppid, pid):
            tree[p].add(c)
        
        # BFS
        res = []
        queue = collections.deque([kill])
        
        while queue:
            curr = queue.popleft()
            res.append(curr)
            for child in tree[curr]:
                queue.append(child)
                
        return res
