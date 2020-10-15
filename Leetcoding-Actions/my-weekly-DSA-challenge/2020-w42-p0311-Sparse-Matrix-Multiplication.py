class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        '''
        T: O(i * j * k); i=#row(A), j=#col(A), k=#col(B)
        S: O(1), ignoring space required to store result
        '''
        AB = [[0] * len(B[0]) for _ in range(len(A))]
        
        for i in range(len(A)):
            for j in range(len(A[0])): # same as len(B)
                if A[i][j] == 0: continue
                for k in range(len(B[0])):
                    if B[j][k] == 0: continue
                    AB[i][k] += A[i][j] * B[j][k]
        return AB




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
