class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        curr = self.root
        stack = []
        stack.append((curr, word))
        
        while stack:
            curr, word = stack.pop()
            if not word:
                if curr.isEnd:
                    return True
            
            elif word[0] in curr.children:
                child = curr.children[word[0]]
                stack.append((child, word[1:]))
                
            elif word[0] =='.':
                for child in curr.children.values():
                    stack.append((child, word[1:]))
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
