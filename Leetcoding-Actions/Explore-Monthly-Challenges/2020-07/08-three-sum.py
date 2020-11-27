class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        out = set()
        nums.sort()
        n = len(nums)
        for i in range(n):
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                j, k = i+1, n-1
                while j < k:
                    if nums[i] + nums[j] + nums[k] == 0:
                        a = [nums[i], nums[j], nums[k]]
                        out.add(tuple(a))
                        j += 1
                    elif nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    else:
                        k -= 1
        return out
        
