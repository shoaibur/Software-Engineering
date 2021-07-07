"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def telemarketers(texts, calls):
    numbers = {} # O(n+m)
    # numbers send/receive texts
    for i in range(len(texts)): # O(n)
        sending = texts[i][0]
        receiving = texts[i][1]
        numbers[sending] = numbers.get(sending, 0) + 1
        numbers[receiving] = numbers.get(receiving, 0) + 1
    # numbers answer calls
    for i in range(len(calls)): # O(m)
        answering = calls[i][1]
        numbers[answering] = numbers.get(answering, 0) + 1
    
    # telemarketers --> calling only, not answering calls or sending/receiving texts
    telemarket_numbers = {} # O(m)
    for i in range(len(calls)): # O(m)
        calling = calls[i][0]
        if calling not in numbers:
            # Avoid storing same number more than once
            telemarket_numbers[calling] = telemarket_numbers.get(calling, 0) + 1
    
    telemarket_numbers = sorted(telemarket_numbers.keys())
    
    # Print possible telemarketers' numbers
    print('These numbers could be telemarketers:')
    for num in telemarket_numbers: # O(m)
        print(num)
    return None

telemarketers(texts, calls)

# Complexity analysis
# Time: O(n+m + q log q) --> traverse texts and calls records and sort distinct numbers q
# Space: O(n+m) --> store numbers in texts and calls records
