class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashsize = 1000
        self.hashset = [[]] * self.hashsize
        
    def hash_function(self, key):
        return key % self.hashsize

    def add(self, key: int) -> None:
        indx = self.hash_function(key)
        if not self.contains(key):
            self.hashset[indx].append(key)

    def remove(self, key: int) -> None:
        indx = self.hash_function(key)
        if self.contains(key):
            self.hashset[indx].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        indx = self.hash_function(key)
        return key in self.hashset[indx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
