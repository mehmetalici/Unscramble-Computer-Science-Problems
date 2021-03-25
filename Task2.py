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

def get_column(record: list, col_idx: int):
    return [row[col_idx] for row in record]

def get_argmax(col: List):
    col = list(map(int, col))  
    return col.index(max(col)) 

caller_idx = 0
duration_idx = 3
duration_col = get_column(calls, duration_idx)
longest_call_idx = get_argmax(duration_col)
longest_call_row = [entry for entry in calls[longest_call_idx]]  

print(f"{longest_call_row[caller_idx]} spent the longest time, {longest_call_row[duration_idx]} seconds, on the phone during September 2016.")