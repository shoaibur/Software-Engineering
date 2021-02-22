# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        celebrity = 0
        for i in range(1, n):
            if knows(celebrity, i):
                celebrity = i
        
        # Check celebrity doesn't know anyone
        for i in range(celebrity):
            if knows(celebrity, i):
                return -1
        # Check everyone knows celebrity
        for i in range(n):
            if i == celebrity: continue
            if not knows(i, celebrity):
                return -1
        
        return celebrity
