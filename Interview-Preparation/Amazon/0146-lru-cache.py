class LRUCache:

    def __init__(self, capacity: int):
        self.cache_size = capacity
        self.cache = {}

    def get(self, key: int) -> int: # O(1)
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1

    def put(self, key: int, value: int) -> None: # O(1)
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.cache_size:
            self.cache.pop( next(iter(self.cache)) ) # list(self.cache.keys())[0]
        self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
