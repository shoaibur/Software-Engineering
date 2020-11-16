class RandomizedSet:
    def __init__(self):
        self.dict = {}
        self.data = []        

    def insert(self, val: int) -> bool:
        if val in self.dict: return False
        self.dict[val] = len(self.data)
        self.data.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        1: 0, 4: 1, 5: 2, 3: 3
              ----        3: 1
        [1 4 5 3] --> [1 3 5]
        """
        if val not in self.dict: return False
        
        remove_val = val
        remove_idx = self.dict[remove_val]
        
        last_val = self.data[-1]
        last_idx = self.dict[last_val]
        
        self.dict[last_val] = remove_idx
        self.dict.pop(remove_val)
        
        self.data[remove_idx] = last_val
        self.data.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.data)
