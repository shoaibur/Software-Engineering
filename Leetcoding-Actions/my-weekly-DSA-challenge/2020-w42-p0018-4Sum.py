class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        T: O(n log n + n^3)
        S: O(1)
        '''
        n = len(nums)
        if n < 4: return []
        nums.sort()
        
        results = set()
        
        for x in range(n):
            for y in range(x+1, n):
                i, j = y + 1, n-1
                while i < j:
                    summ = nums[x] + nums[y] + nums[i] + nums[j]
                    if summ == target:
                        results.add((nums[x],nums[y], nums[i], nums[j]))
                        i += 1
                    elif summ < target:
                        i += 1
                    else:
                        j -= 1
        return results
