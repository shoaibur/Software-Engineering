class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        T: O(n^2) --> O(n) for looping all candidates and O(n) for dfs backtracking.
        S: O(1)
        '''
        n = len(candidates)
        result = []
        
        def dfs(num, currSum, i):
            if currSum == target:
                result.append(num)
            elif currSum < target:
                for j in range(i, n):
                    dfs(num + [candidates[j]], currSum + candidates[j], j)
        
        for i in range(n):
            dfs([candidates[i]], candidates[i], i)
            
        return result
