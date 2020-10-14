class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        '''
        T: O(mA * nA + mB * nB)
        S: O(mA + nB)
        '''
        def sparseDotProduct(a, b):
            a = {i: num for i, num in enumerate(a) if num != 0}
            b = {i: num for i, num in enumerate(b) if num != 0}
            prodSum = 0
            for i in a:
                if i in  b:
                    prodSum += a[i] * b[i]
            return prodSum
        # We need to access colums of B, so transpose
        B[:] = [*zip(*B)]
        
        # Dot product each row of A with each column of B (each row of B after transpose)
        AB = []
        for i in range(len(A)):
            a = A[i]
            temp = []
            for j in range(len(B)):
                b = B[j]
                prodSum = sparseDotProduct(a, b)
                temp.append(prodSum)
            AB.append(temp)
            
        return AB
