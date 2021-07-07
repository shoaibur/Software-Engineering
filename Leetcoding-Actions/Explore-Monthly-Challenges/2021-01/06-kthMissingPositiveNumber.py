class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        Number of missing element at index i = 
        = arr[0] - 1 + arr[idx] - arr[0] - idx = 
        = arr[idx] - idx - 1
        
        T: O(log n) and O(1)
        '''
        
        def countMissing(idx):
            return arr[idx] - idx - 1
        
        if k < arr[0]: return k
        
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if countMissing(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        
        return arr[lo - 1] + k - countMissing(lo - 1)
