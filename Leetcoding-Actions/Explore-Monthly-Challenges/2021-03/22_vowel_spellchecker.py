class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        '''
        T: O(mn) and S: O(mn)
        Case 1: query exist in wordlist
        Case 2: query match upto captial letter
        Case 3: query match upto vowel error
        '''
        words = set(wordlist)
        words_case_insensitive = defaultdict(list)
        vowels = defaultdict(list)
        
        for word in wordlist: 
            key = word.lower()
            words_case_insensitive[key].append(word)
            for c in "aeiou": key = key.replace(c, "*")
            vowels[key].append(word)
        
        ans = []
        for word in queries: 
            if word in words: # Case 1
                ans.append(word)
            else: 
                key = word.lower()
                if key in words_case_insensitive: # Case 2
                    ans.append(words_case_insensitive[key][0])
                else: # Case 3
                    for c in "aeiou":
                        key = key.replace(c, "*")
                    if key in vowels:
                        ans.append(vowels[key][0])
                    else:
                        ans.append("")
        return ans
