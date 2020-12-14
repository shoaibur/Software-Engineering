class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        def dfs(start_ind, path):
            if start_ind >= len(s):
                result.append(path)
                
            for l in range(len(s) - start_ind):
                if s[start_ind:start_ind+l+1] == s[start_ind:start_ind+l+1][::-1]:
                    dfs(start_ind + l + 1, path + [s[start_ind:start_ind + l + 1]] )
        
        dfs(0,[])
        return result
