import datetime
import hashlib

class Block:
    def __init__(self, timestamp, value, previous_hash):
        self.timestamp = timestamp
        self.value = value
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(value)
        self.next = None

    def calc_hash(self, data):
        hash_str = data.encode('utf-8')
        sha = hashlib.sha256()
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None

    def append(self, value):
        if self.head is None:
            self.head = Block(datetime.datetime.now(), value, None)
            return
        tail = self.head
        while tail.next:
            tail = tail.next
        tail.next = Block(datetime.datetime.now(), value, tail.hash)
    
    def search(self, value):
        if self.head is None: return None
        tail = self.head
        while tail:
            if tail.value == value:
                return True
            tail = tail.next
        return 'Value not found!'
    
    def to_list(self):
        if self.head is None: return [],[],[],[]
        tail = self.head
        timestamps, values, prev_hashes, hashes = [], [], [], []
        while tail:
            timestamps.append(tail.timestamp)
            values.append(tail.value)
            prev_hashes.append(tail.previous_hash)
            hashes.append(tail.hash)
            tail = tail.next
        return timestamps, values, prev_hashes, hashes

# Test cases

# Create a blockchain using append
items = ['1', '2', '3', '4', '5']
blockchain = BlockChain()
for item in items:
    blockchain.append(item)

# to_list
timestamps, values, prev_hashes, hashes = blockchain.to_list()

print(values)
# ['1', '2', '3', '4', '5']

for i in range(len(hashes)-1):
    print(prev_hashes[i+1] == hashes[i])
# True True True True 

# Search
print(blockchain.search('3'))
# True

print(blockchain.search('6'))
# Value not found!


# Edge case
items = []
blockchain = BlockChain()
for item in items:
    blockchain.append(item)

# to_list
timestamps, values, prev_hashes, hashes = blockchain.to_list()

print(values)
# []

for i in range(len(hashes)-1):
    print(prev_hashes[i+1] == hashes[i])
# 

# Search
print(blockchain.search('3'))
# None

print(blockchain.search('6'))
# None
