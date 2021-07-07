# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        11 12 13 14 15 16 17
        21 22 23 24 25 26 27
        31 32 33 34 35 36 37
        41 42 43 44 45 46 47
        51 52 53 54 55 56 57
        61 62 63 64 65 66 67
        71 72 73 74 75 76 77
        """
        x1 = rand7()
        x2 = rand7()
        
        while (x1 == 6 and x2 >= 6) or x1 == 7:
            x1 = rand7()
            x2 = rand7()
        return (7 * (x1 - 1) + x2) % 10 + 1
