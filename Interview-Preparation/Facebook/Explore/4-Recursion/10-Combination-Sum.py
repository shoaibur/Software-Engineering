class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        
        def dfs(nums, currSum, i):
            if currSum == target:
                combinations.append(nums)
            elif currSum < target:
                for j in range(i, len(candidates)):
                    dfs(nums+[candidates[j]], currSum+candidates[j], j)
        
        for i in range(len(candidates)):
            dfs([candidates[i]], candidates[i], i)
            
        return combinations
