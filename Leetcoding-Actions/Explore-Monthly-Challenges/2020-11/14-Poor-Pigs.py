class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        '''
        states ^ pigs >= buckets
        pigs >= log(buckets) / log(states)
        T: O(1) and S: O(1)
        '''
        states = minutesToTest // minutesToDie + 1
        return math.ceil(math.log(buckets) / math.log(states))
