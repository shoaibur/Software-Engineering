class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        result = []
        counter = defaultdict(list)
        for idx in sorted(B, reverse=True):
            if A[-1] > idx: 
                counter[idx].append(A.pop())
        for idx in B:
            if counter[idx]:
                result.append(counter[idx].pop())
            else:
                result.append(A.pop())
        return result
