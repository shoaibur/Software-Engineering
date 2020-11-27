class Solution:
    def toGoatLatin(self, S: str) -> str:
        
        words = S.split()
        sentence = ''
        for i, word in enumerate(words):
            if word[0] in 'aeiouAEIOU':
                word = word + 'ma' + 'a' * (i+1)
            else:
                word = word[1:] + word[0] + 'ma' + 'a' * (i+1)
            space = ' ' if i != len(words)-1 else ''
            sentence += word + space
        return sentence
