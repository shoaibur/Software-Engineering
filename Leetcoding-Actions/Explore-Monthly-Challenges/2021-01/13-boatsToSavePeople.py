class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat = 0
        i, j = 0, len(people)-1
        while i <= j:
            if people[i] + people[j] > limit:
                boat += 1
                j -= 1
            else:
                i += 1
                j -= 1
                boat += 1
        return boat
