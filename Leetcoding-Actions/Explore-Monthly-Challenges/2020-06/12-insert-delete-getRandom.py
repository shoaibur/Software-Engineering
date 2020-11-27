# Design a data structure that supports all following operations in average O(1) time.
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. Each element must have the same probability of being returned.

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}
        self.data = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.hash:
            self.hash[val] = len(self.data)
            self.data.append(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hash:
            return False
        
        remove_value = val
        last_value = self.data[-1]
        remove_index = self.hash[remove_value]
        last_index = self.hash[last_value]
        
        self.hash[last_value] = remove_index
        self.hash.pop(remove_value)
        
        self.data[remove_index] = last_value
        self.data.pop()
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)
        
