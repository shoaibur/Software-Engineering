class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for word in strs:
            count = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                count[idx] += 1
            if tuple(count) in group:
                group[tuple(count)].append(word)
            else:
                group[tuple(count)] = [word]
                
        return [val for _, val in group.items()]
