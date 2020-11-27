class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        def permute(nums):
            permutations = []
            if len(nums) <= 1: return [nums]
            for i in range(len(nums)):
                first = [nums[i]]
                rem = nums[:i] + nums[i+1:]
                for p in permute(rem):
                    permutations.append(first + p)
            return permutations
        
        permutations = permute(A)
        result = ''
        for item in permutations:
            hh = str(item[0]) + str(item[1])
            mm = str(item[2]) + str(item[3])
            if hh <= '23' and mm <= '59' and (hh+':'+mm) > result:
                result = hh + ':' + mm
        return result
