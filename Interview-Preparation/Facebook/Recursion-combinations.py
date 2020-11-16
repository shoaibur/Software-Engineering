class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # nums = range(1, n+1)
        
        combinations = []
        
        q = collections.deque()
        q.append(([], 0))
        
        while q:
            temp, curr = q.popleft()
            if len(temp) == k:
                combinations.append(temp)
                
            for i in range(curr, n):
                q.append((temp+[i+1], i+1))
                # q.append((temp+[nums[i]], i+1))
        return combinations
