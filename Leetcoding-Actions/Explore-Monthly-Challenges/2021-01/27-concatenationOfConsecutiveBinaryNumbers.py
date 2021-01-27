class Solution:
    def concatenatedBinary(self, n: int) -> int:
        decimal = 0
        k = 0
        binary = ""
        for i in range(1, n+1):
            binary += bin(i)[2:]
        decimal = int(binary, 2)
        return decimal % (1000000007)
