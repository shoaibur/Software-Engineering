class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = {}
        count = 0
        for t in time:
            if t % 60 == 0:
                count += d.get(0, 0)
            else:
                count += d.get(60 - t % 60, 0)
            d[t % 60] = d.get(t % 60, 0) + 1
        return count
