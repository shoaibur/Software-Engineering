class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        nums = [i for i in range(1,10)]
        
        result = []
        
        out = [[]]
        for num in nums:
            temp = []
            for item in out:
                comb = item + [num]
                if len(comb) == k:
                    if sum(comb) == n:
                        result.append(comb)
                    continue
                temp.append(comb)
            out += temp
            
        return result
