class Solution:

    def __init__(self, weights: List[int]):
        cumsum = [weights[0]]
        for weight in weights[1:]:
            cumsum.append(cumsum[-1]+weight)
        self.cumsum = cumsum
        self.sum = self.cumsum[-1]

    def pickIndex(self) -> int:
        r = random.randint(1, self.sum)
        # for i in range(len(self.cumsum)):
        #     # O(1)
        #     if self.cumsum[i] >= r:
        #         return i
        # O(log n)
        return self.binary_search(self.cumsum, r)
    
    def binary_search(self, nums, value):
        lo, hi = 0, len(nums)-1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] >= value:
                hi = mid
            else:
                lo = mid + 1
        return lo


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
