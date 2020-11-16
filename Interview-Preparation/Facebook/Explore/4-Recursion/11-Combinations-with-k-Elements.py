class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        
        combinations = []
        
        out = [[]]
        for num in nums:
            temp = []
            for item in out:
                comb = item + [num]
                if len(comb) == k:
                    combinations.append(comb)
                    continue
                temp.append(comb)
            out += temp
            
        return combinations
