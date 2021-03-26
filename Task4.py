"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from os import O_APPEND

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
A telephone company wants to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def get_unique(arr: list):
  return list(set(arr))


def get_col_unique(record: list, col_idx: int):
  return get_unique([row[col_idx] for row in record])


def check_numbers(list_to_be_checked, candidate_numbers: list):
    candidates_remained = []
    for number in candidate_numbers:
        if not number in list_to_be_checked:
            candidates_remained.append(number)
    return candidates_remained


def get_possible_telemarketers(candidate_numbers: list):
    unique_textees = get_col_unique(texts, col_idx=1)
    unique_callees = get_col_unique(calls, col_idx=1)
    unique_texters = get_col_unique(texts, col_idx=0)

    checklists = (unique_textees, unique_callees, unique_texters)

    candidates_remaining = candidate_numbers[:]
    for checklist in checklists:
        candidates_remaining = check_numbers(checklist, candidates_remaining) 
    return sorted(candidates_remaining)


unique_callers = get_col_unique(calls, col_idx=0)
print("These are the possible telemarketers:")
print("\n".join(get_possible_telemarketers(unique_callers)))