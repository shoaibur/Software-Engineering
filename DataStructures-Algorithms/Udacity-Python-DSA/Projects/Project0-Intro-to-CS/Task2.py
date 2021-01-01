"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def longest_time_numbers(calls):
    max_duration = 0
    # Traverse calls records
    for i in range(len(calls)):
        duration = int(calls[i][3]) # 4th column - duration in seconds
        if duration > max_duration: # check if current call is greater than max_duration
            max_duration = duration
            calling = calls[i][0]
            answering = calls[i][1]
    return calling, answering, max_duration

calling, answering, max_duration = longest_time_numbers(calls)

print(f'{calling} and {answering} spent the longest time, {max_duration} seconds, on the phone during September 2016.')

# Complexity analysis
# m = number of records in the calls
# Time: O(m) --> traverse call records
# Space: O(1) --> No additional (except a constant) space is used

