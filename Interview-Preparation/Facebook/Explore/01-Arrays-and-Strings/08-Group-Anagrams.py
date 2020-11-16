class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return strs
        anagrams = {}
        for word in strs:
            counter = [0] * 26
            for char in word:
                counter[ord(char)-ord('a')] += 1
            if tuple(counter) in anagrams:
                anagrams[tuple(counter)].append(word)
            else:
                anagrams[tuple(counter)] = [word]
        return [val for _, val in anagrams.items()]
