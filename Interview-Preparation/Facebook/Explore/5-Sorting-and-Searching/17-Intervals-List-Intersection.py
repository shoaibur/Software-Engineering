    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        
        def overlap(i1, i2):
            if i1[0] > i2[0]:
                i1, i2 = i2, i1
            merged = []
            if i1[1] >= i2[0]:
                merged = [max(i1[0], i2[0]), min(i1[1], i2[1])]
            return merged
        
        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            i1 = A[i]
            i2 = B[j]
            merged = overlap(i1, i2)
            if merged:
                result.append(merged)
            if i1[1] < i2[1]:
                i += 1
            else:
                j += 1
        return result
