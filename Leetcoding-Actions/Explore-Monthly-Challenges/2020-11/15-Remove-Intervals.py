class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        lo, hi = toBeRemoved
        result = []
        for interval in intervals:
            a, b = interval
            diffA = lo - a
            diffB = b - hi
            
            if diffA > 0:
                result.append([a, min(lo, b)])
            if diffB > 0:
                result.append([max(hi,a),b])

        return result
