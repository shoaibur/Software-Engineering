import heapq

def char_frequency(message):
    d = {}
    for char in message:
        d[char] = d.get(char, 0) + 1
    return d

def get_tree_children(d):
    '''d is char_frequency dict map'''
    pq = [] # Priority queue
    for item in d.items():
        heapq.heappush(pq, [item])
    # Get left (lowest freq) and right (2nd lowest freq) children
    while (len(pq) > 1):
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        child_left, freq_left = left[0]
        child_right, freq_right = right[0]
        node = [(child_left + child_right, freq_left + freq_right), left, right]
        heapq.heappush(pq, node)
    return pq.pop()

def get_map_from_tree(tree, maps={}, prefix=''):
    # Base case
    if (len(tree) == 1):
        label, freq = tree[0]
        maps[label] = prefix
    else: # Recursively create the maps by adding 0/1
        value, left, right = tree
        get_map_from_tree(left, maps, prefix + '0')
        get_map_from_tree(right, maps, prefix + '1')
    return maps

def huffman_encoding(message):
    tree = get_tree_children(char_frequency(message))
    maps = get_map_from_tree(tree)
    encoded_message = ''.join([ maps[letter] for letter in message ])
    return encoded_message, tree

def huffman_decoding(encoded_message, tree):
    code = tree
    decoded_message = []

    for bit in encoded_message:
        # Get appropriate code
        if (bit == '0'):
            code = code[1]
        else:
            code = code[2]
        # Decode message from the code
        if (len(code) == 1):
            label, freq = code[0]
            decoded_message.append(label)
            code = tree # Reset code for next bit
    return ''.join(decoded_message)

# Tests
if __name__ == "__main__":
    
    # Test 1
    print('\nTest 1---------------------------')
    message = "The bird is the word"

    print (f'Original message: {message}\n')
    encoded_message, tree = huffman_encoding(message)
    print(f'Size of original message: {len(message)}\n'
          f'Size of encoded message: {len(encoded_message)}\n')

    print ("Encoded message: {}\n".format(encoded_message))

    decoded_message = huffman_decoding(encoded_message, tree)

    print (f'Size of decoded message: {len(decoded_message)}\n')
    print (f'Decoded message: {decoded_message}')
    
#     Test 1---------------------------
#     Original message: The bird is the word

#     Size of original message: 20
#     Size of encoded message: 144

#     Encoded message: 000000000010000001000000010000000000000000000010000010001000000001000000000000000010010000000000001000000100000001000000000001000010001000000001

#     Size of decoded message: 20

#     Decoded message: The bird is the word
    
    
    
    # Test 2 # Message with punctuations
    print('\nTest 2---------------------------')
    message = "Let's create a peaceful world!"

    print (f'Original message: {message}\n')
    encoded_message, tree = huffman_encoding(message)
    print(f'Size of original message: {len(message)}\n'
          f'Size of encoded message: {len(encoded_message)}\n')

    print ("Encoded message: {}\n".format(encoded_message))

    decoded_message = huffman_decoding(encoded_message, tree)

    print (f'Size of decoded message: {len(decoded_message)}\n')
    print (f'Decoded message: {decoded_message}')
    
#     Test 2---------------------------
#     Original message: Let's create a peaceful world!

#     Size of original message: 30
#     Size of encoded message: 294

#     Encoded message: 000000000000010000000001001000000000000001000100000000000000000000000000010000100000000010000000000001001000000000100000000000000000000000000001000000000000000000000100000000010000000000001000000000001000000000100000000101000000010000000000000000100000010000100000001000000000010000000000000001

#     Size of decoded message: 30

#     Decoded message: Let's create a peaceful world!
    
    
    # Test 3 # Empty message
    print('\nTest 3---------------------------')
    message = " "

    print (f'Original message: {message}\n')
    encoded_message, tree = huffman_encoding(message)
    print(f'Size of original message: {len(message)}\n'
          f'Size of encoded message: {len(encoded_message)}\n')

    print ("Encoded message: {}\n".format(encoded_message))

    decoded_message = huffman_decoding(encoded_message, tree)

    print (f'Size of decoded message: {len(decoded_message)}\n')
    print (f'Decoded message: {decoded_message}')
    
#     Test 3---------------------------
#     Original message:  

#     Size of original message: 1
#     Size of encoded message: 0

#     Encoded message: 

#     Size of decoded message: 0

#     Decoded message: 


    # Test 4 # String with repeating character
    print('\nTest 4---------------------------')
    message = " aaaaaaaa "

    print (f'Original message: {message}\n')
    encoded_message, tree = huffman_encoding(message)
    print(f'Size of original message: {len(message)}\n'
          f'Size of encoded message: {len(encoded_message)}\n')

    print ("Encoded message: {}\n".format(encoded_message))

    decoded_message = huffman_decoding(encoded_message, tree)

    print (f'Size of decoded message: {len(decoded_message)}\n')
    print (f'Decoded message: {decoded_message}')
    
#     Test 4---------------------------
#     Original message:  aaaaaaaa 

#     Size of original message: 10
#     Size of encoded message: 10

#     Encoded message: 0111111110

#     Size of decoded message: 10

#     Decoded message:  aaaaaaaa 
