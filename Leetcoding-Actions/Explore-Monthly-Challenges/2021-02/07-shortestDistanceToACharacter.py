class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        '''
        T: O(n) and S: O(n)
        '''
        q = deque()
        for i,char in enumerate(s):
            if char == c:
                q.append(i)
        
        ans = []
        i = q.popleft()
        for j, char in enumerate(s):
            if not q:
                dist = abs(j - i)
            else:
                dist1 = abs(j - i)
                dist2 = abs(j - q[0])
                if dist2 < dist1:
                    dist = dist2
                    i = q.popleft()
                else:
                    dist = dist1
            ans.append(dist)
                    
        return ans
