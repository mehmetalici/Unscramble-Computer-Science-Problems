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

TELEMARKET_PREFIX = 140


class PrefixTypes:
  MOBILE = 0
  FIXED = 1
  TELEMARKET = 2


class UndefinedPrefixException(Exception):
  def __init__(self, *args: object) -> None:
      super().__init__(*args)


def get_unique(arr: list):
  return set(arr)


def get_column(record: list, col_idx: int):
  return [row[col_idx] for row in record]


def get_prefix_type(number: str):

  if number[0] == '(' and ')' in number[1:]:
    return PrefixTypes.FIXED

  if ' ' in number and int(number[0]) in [7, 8, 9]:  
    return PrefixTypes.MOBILE

  if number[:3] == TELEMARKET_PREFIX:  
    return PrefixTypes.TELEMARKET

  raise UndefinedPrefixException


def get_mobile_prefix(number: str):
  try:
    type = get_prefix_type(number)  
  except UndefinedPrefixException:
    #print(f"Warning: {number} contains unknown prefix. Skipping...")
    return

  if type == PrefixTypes.FIXED:
    start_idx = 1
    try:
      end_idx = number.index(')')  
    except ValueError:
      #print(f"Warning: {number} contains unended paranthesis. Skipping...")
      return
    return number[start_idx:end_idx]
  
  if type == PrefixTypes.MOBILE:  
    return number[0:4]  

  if type == PrefixTypes.TELEMARKET:
    return TELEMARKET_PREFIX  


callee_col = get_column(calls, col_idx=1)
unique_prefixes = get_unique([get_mobile_prefix(number) for number in callee_col])
print("\n".join(sorted(unique_prefixes)))









