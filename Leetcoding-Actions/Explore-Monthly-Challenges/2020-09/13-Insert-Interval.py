class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def binarySearch(nums, target):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if nums[mid] >= target:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        nums = [interval[0] for interval in intervals]
        i = binarySearch(nums, newInterval[0])
        intervals.insert(i, newInterval)
        
        def merge(intervals):
            result = [intervals[0]]
            i1 = result[-1]
            for i2 in intervals[1:]:
                if i1[1] >= i2[0]:
                    merged = [min(i1[0], i2[0]), max(i1[1], i2[1])]
                    result[-1] = merged
                else:
                    result.append(i2)
                i1 = result[-1]
            return result
        return merge(intervals)
