class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_index = {char: i for i, char in enumerate(S)}
        
        result = []
        start, end = 0, 0
        
        for i, char in enumerate(S):
            end = max(end, last_index[char])
            if i == end:
                result.append(end - start + 1)
                start = end + 1
        return result
    
