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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


# Part A: If I understand correctly, this problem is asking to find the codes of the calling numbers, who called to Bangalore or to the code: '(080)'

def call_to_fixed_lines(calls, code='(080)'):
    out = []
    print('The numbers called by people in Bangalore have codes:')
    for i in range(len(calls)):
        calling = calls[i][0]
        answering = calls[i][1]
        if answering.startswith(code):
            if '(' in calling:
                out.append( calling.split(')')[0] + ')' )
                #print( calling.split(')')[0] + ')' ) # digits within parenthesis, including parenthesis
            elif ' ' in calling and calling.startswith(('7','8','9')):
                out.append(calling[:4])
                #print(calling[:4]) # first 4 digits
            elif calling.startswith('140'):
                out.append(calling[:3])
                #print(calling[:3]) # first 3 digits, i.e., 140
    return sorted(list(set(out)))

call_to_fixed_lines(calls)

# Complexity analysis
# Time: O(m + q log q) --> traverse calls records and sort the distinct codes (q)
# Space: O(m) --> storing codes from calls records




# Part B
def fixed2fixed(calls, code='(080)'):
    b2b_fixed_count = 0 # O(1)
    b2any_fixed_count = 0
    for i in range(len(calls)): # O(m)
        calling = calls[i][0]
        answering = calls[i][1]
        if calling.startswith(code) and answering.startswith(code):
            b2b_fixed_count += 1
        if calling.startswith(code) and answering.startswith('('):
            b2any_fixed_count += 1
    return (b2b_fixed_count / b2any_fixed_count) * 100

percentage = fixed2fixed(calls)
print(f'{percentage:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.')

# Complexity analysis
# Time: O(m) --> traverse calls records
# Space: O(1) --> only constant space is used

