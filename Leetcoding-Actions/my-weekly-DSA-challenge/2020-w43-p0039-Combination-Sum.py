class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        T: O(n * O(dfs))
        Height of the tree = target / min(candidates), so total number of
        nodes in the tree = n ^ height of tree = n ^ (T / m). So,
        T: O(n . n^(t/m)) = O(n ^ (T / m + 1))
        S: O(T / m)
        '''
        n = len(candidates)
        result = []
        
        def dfs(num, curSum, i):
            if curSum == target:
                result.append(num)
            elif curSum < target:
                for j in range(i, n):
                    dfs(num + [candidates[j]], curSum + candidates[j], j)
        
        for i in range(n):
            dfs([candidates[i]], candidates[i], i)
            
        return result
