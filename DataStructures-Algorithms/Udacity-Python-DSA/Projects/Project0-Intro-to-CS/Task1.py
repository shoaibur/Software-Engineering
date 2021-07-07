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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def unique_numbers(texts, calls):
    numbers = {} # Hash table / dictionary
    # Traverse texts records
    for i in range(len(texts)):
        sending = texts[i][0]
        receiving = texts[i][1]
        numbers[sending] = numbers.get(sending, 0) + 1
        numbers[receiving] = numbers.get(receiving, 0) + 1
    # Traverse calls records
    for i in range(len(calls)):
        calling = calls[i][0]
        receiving = calls[i][1]
        numbers[calling] = numbers.get(calling, 0) + 1
        numbers[receiving] = numbers.get(receiving, 0) + 1
    return numbers

numbers = unique_numbers(texts, calls)

print(f'There are {len(numbers)} different telephone numbers in the records')


# Complexity analysis
# n = number of records in texts
# m = number of records in calls
# Time: O(m + n) --> traverse both texts and calls records
# Space: O(m + n) --> to save the dictionary "numbers"
