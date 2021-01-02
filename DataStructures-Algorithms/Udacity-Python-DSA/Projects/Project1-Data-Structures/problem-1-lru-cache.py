class LRUcache:
    def __init__(self, capacity=5):
        self.cache_size = capacity
        self.cache_maps = {}
        
    # Idea for get/put operations: keys of the python dict are
    # stored in the order at which they were added, e.g. first
    # added key is dict.keys()[0], and so on.
    
    def get(self, key):
        if key in self.cache_maps:
            # If hits, add it to the least recently used items.
            # Retrieve the value, pop the key, and add the key.
            value = self.cache_maps[key]
            self.cache_maps.pop(key)
            self.cache_maps[key] = value
            # Return value
            return value
        # If doesn't hit, return -1
        return -1
    
    def put(self, key, value):
        # If key already in cache, pop that out.
        if key in self.cache_maps:
            self.cache_maps.pop(key)
        # If not in cache and cache reaches its capacity,
        # pop the earliers key added, i.e. key[0], which
        # can be done using next and iter in O(1) time.
        elif len(self.cache_maps) == self.cache_size:
            self.cache_maps.pop( next(iter(self.cache_maps)) )
        # And, add the key, value to cache
        self.cache_maps[key] = value
        #print(self.cache_maps.keys())
        return None

# Test cases
import random
random.seed(18)
cache = LRUcache(5)
requests = [1,2,3,4,1,4,9,1,3,5,3]
for i,request in enumerate(requests):
    print(f'operation: put({request},{request})', end='\t')
    print('output:', cache.put(request, request), end='\t')
    print(f'cache keys: {list(cache.cache_maps.keys())}')
    if (i+1) % 2 == 0:
        rand = random.randint(0,9)
        print(f'operation: get({rand})', end='\t')
        print('output:', cache.get(rand), end='\t')
        print(f'cache keys: {list(cache.cache_maps.keys())}')
        
# operation: put(1,1)	output: None	cache keys: [1]
# operation: put(2,2)	output: None	cache keys: [1, 2]
# operation: get(2)	output: 2	cache keys: [1, 2]
# operation: put(3,3)	output: None	cache keys: [1, 2, 3]
# operation: put(4,4)	output: None	cache keys: [1, 2, 3, 4]
# operation: get(1)	output: 1	cache keys: [2, 3, 4, 1]
# operation: put(1,1)	output: None	cache keys: [2, 3, 4, 1]
# operation: put(4,4)	output: None	cache keys: [2, 3, 1, 4]
# operation: get(7)	output: -1	cache keys: [2, 3, 1, 4]
# operation: put(9,9)	output: None	cache keys: [2, 3, 1, 4, 9]
# operation: put(1,1)	output: None	cache keys: [2, 3, 4, 9, 1]
# operation: get(5)	output: -1	cache keys: [2, 3, 4, 9, 1]
# operation: put(3,3)	output: None	cache keys: [2, 4, 9, 1, 3]
# operation: put(5,5)	output: None	cache keys: [4, 9, 1, 3, 5]
# operation: get(3)	output: 3	cache keys: [4, 9, 1, 5, 3]
# operation: put(3,3)	output: None	cache keys: [4, 9, 1, 5, 3]


# Edge case 1: Empty cache
import random
random.seed(18)
cache = LRUcache(0)
requests = [1,2,3,4,1,4,9,1,3,5,3]
for i,request in enumerate(requests):
    print(f'operation: put({request},{request})', end='\t')
    print('output:', cache.put(request, request), end='\t')
    print(f'cache keys: {list(cache.cache_maps.keys())}')
    if (i+1) % 2 == 0:
        rand = random.randint(0,9)
        print(f'operation: get({rand})', end='\t')
        print('output:', cache.get(rand), end='\t')
        print(f'cache keys: {list(cache.cache_maps.keys())}')
        
# operation: put(1,1)	output: No cache is available	cache keys: []
# operation: put(2,2)	output: No cache is available	cache keys: []
# operation: get(2)	output: No cache is available	cache keys: []
# operation: put(3,3)	output: No cache is available	cache keys: []
# operation: put(4,4)	output: No cache is available	cache keys: []
# operation: get(1)	output: No cache is available	cache keys: []
# operation: put(1,1)	output: No cache is available	cache keys: []
# operation: put(4,4)	output: No cache is available	cache keys: []
# operation: get(7)	output: No cache is available	cache keys: []
# operation: put(9,9)	output: No cache is available	cache keys: []
# operation: put(1,1)	output: No cache is available	cache keys: []
# operation: get(5)	output: No cache is available	cache keys: []
# operation: put(3,3)	output: No cache is available	cache keys: []
# operation: put(5,5)	output: No cache is available	cache keys: []
# operation: get(3)	output: No cache is available	cache keys: []
# operation: put(3,3)	output: No cache is available	cache keys: []


# Edge case 2: Empty request
import random
random.seed(61)
cache = LRUcache(5)
requests = []
for i,request in enumerate(requests):
    print(f'operation: put({request},{request})', end='\t')
    print('output:', cache.put(request, request), end='\t')
    print(f'cache keys: {list(cache.cache_maps.keys())}')
    if (i+1) % 2 == 0:
        rand = random.randint(0,9)
        print(f'operation: get({request}', end='\t')
        print('output:', cache.get(rand), end='\t')
        print(f'cache keys: {list(cache.cache_maps.keys())}')
        
# Nothing is printed out
