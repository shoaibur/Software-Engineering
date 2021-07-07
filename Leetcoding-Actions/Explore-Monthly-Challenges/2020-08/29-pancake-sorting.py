class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        result = []
        def flip(idx):
            for i in range(0, idx//2+1):
                temp = A[i]
                A[i] = A[idx-i]
                A[idx-i] = temp
        for i in range(len(A)-1, 0, -1):
            for j in range(1, i+1):
                if A[j] == i+1:
                    flip(j)
                    result.append(j+1)
                    break
            flip(i)
            result.append(i+1)
        return result
