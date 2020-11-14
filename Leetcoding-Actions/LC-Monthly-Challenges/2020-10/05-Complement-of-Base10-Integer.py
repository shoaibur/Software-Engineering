class Solution:
    def bitwiseComplement(self, N: int) -> int:
        '''
        T: O(32) = O(1), max 32 bits in binary
        S: O(32) = O(1)
        '''
        binary = bin(N)[2:]
                
        binary_complement = ''
        for digit in binary:
            digit = '1' if digit=='0' else '0'
            binary_complement += digit
        
        return int(binary_complement,2)
