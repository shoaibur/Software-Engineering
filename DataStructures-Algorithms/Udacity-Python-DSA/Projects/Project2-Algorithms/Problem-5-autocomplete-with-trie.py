## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie
        node = self.root
        for char in word: # O(n*m) in time
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isword = True

    def find(self, prefix):
        ## Find the Trie node that represents this prefix
        node = self.root
        for char in prefix:  # O(n) in time
            if char not in node.children:
                return False
            node = node.children[char]
        return node


# # Finding Suffixes
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.isword = False
        self.children = {}
    
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:  # O(n) in time
            self.children[char] = TrieNode()
        
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        sfxlist = []
        for char, node in self.children.items():  # O(n) in time
            if node.isword:
                sfxlist.append(suffix+char)
            if node.children:
                sfxlist += node.suffixes(suffix+char)
        return sfxlist


# # Testing it all out
MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
paragraph = 'Before we start let us reiterate the key components of a Trie or Prefix Tree.            A trie is a tree-like data structure that stores a dynamic set of strings. Tries             are commonly used to facilitate operations like predictive text or autocomplete             features on mobile phones or web search.'
paragraph = paragraph.replace('.!?','')
wordList = paragraph.split()

for word in wordList:
    MyTrie.insert(word)


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact
def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');


