# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        '''
        T: O(log n) and S: O(1)
        '''
        # Max limit of array range
        hi = 1
        while reader.get(hi) <= target:
            hi *= 2
        # Binary search between lo and hi
        lo = 0
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if reader.get(mid) >= target:
                hi = mid
            else:
                lo = mid + 1
        if reader.get(lo) == target:
            return lo
        return -1
