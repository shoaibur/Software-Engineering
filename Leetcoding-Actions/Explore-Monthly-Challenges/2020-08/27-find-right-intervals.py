
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        arr = []
        n = len(intervals)
        for i in range(n):
            arr.append([intervals[i], i])
        arr.sort()
        
        def binarySearch(target):
            if arr[n-1][0][0] < target: return -1
            lo, hi = 0, n-1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if arr[mid][0][0] >= target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            return arr[lo][1]
                
        result = [-1] * n
        for i in range(n):
            result[i] = binarySearch(intervals[i][1])
        return result
