class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        '''
        T: O(#words_in_A * #unique_chars_in_all_word_of_B + #words_in_B) =
           O(#words_in_A * 26 + #words_in_B) = O(#words_in_A + #words_in_B)
        S: O(#unique_chars_in_all_word_of_B  + #unique_chars_in_longest_word_in_A) =
           O(26  + 26) = O(1)
        '''
        b_count = Counter()
        for word in B:
            b_count |= Counter(word)
        
        ans = []
        for word in A:
            a_count = Counter(word)
            if all(a_count[char] >= b_count[char] for char in b_count):
                ans.append(word)
        
        return ans
