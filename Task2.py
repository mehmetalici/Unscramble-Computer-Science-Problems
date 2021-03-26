"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from typing import List
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

def add_to_dict(d: dict, key: str, value: int):
    try:
        d[key] += value
    except KeyError:
        d[key] = value

def get_longest_time(calls: list):
    durations = {}
    for call in calls:
        caller, callee, duration = call[0], call[1], call[3]
        for number in [caller, callee]:
            add_to_dict(durations, number, int(duration))

    longest_duration_number = max(durations, key=lambda key: durations[key])
    longest_duration = durations[longest_duration_number]
    return (longest_duration_number, longest_duration)

number, duration = get_longest_time(calls)
print(f"{number} spent the longest time, {duration} seconds, on the phone during September 2016.")


