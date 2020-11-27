class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.endWord = False
        self.children = [None] * 26
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self
        for char in word:
            indx = ord(char) - ord('a')
            if curr.children[indx] == None:
                curr.children[indx] = WordDictionary()
            curr = curr.children[indx]
        curr.endWord = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        curr = self
        for i in range(len(word)):
            char = word[i]
            indx = ord(char) - ord('a')
            if char == '.':
                for ch in curr.children:
                    if ch != None and ch.search(word[i+1:]):
                        return True
                return False
            if curr.children[indx] == None:
                return False
            curr = curr.children[indx]
        return curr != None and curr.endWord
    
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
