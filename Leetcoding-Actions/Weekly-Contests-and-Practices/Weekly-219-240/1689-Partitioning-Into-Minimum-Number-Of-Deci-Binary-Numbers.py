class Solution:
    def minPartitions(self, n: str) -> int:
        '''
        32 = 11
        22 = 11
        11 = 
        82734 = 11111
        71623 = 11111
        60512 = 10111
        50401 = 10101
        40300 = 10100
        30200 = 10100
        20100 = 10100
        10000 = 10000
        '''
        # count = 0
        # m = int(n)
        # while int(n) > 0:
        #     b = ""
        #     for digit in n:
        #         if digit != "0":
        #             b += "1"
        #         else:
        #             b += "0"
        #     count += 1
        #     if count == 9:
        #         return count
        #     m -= int(b)
        #     n = str(m)
        # return count
        count = 0
        for digit in n:
            count = max(int(digit), count)
            if count == 9:
                return count
        return count
