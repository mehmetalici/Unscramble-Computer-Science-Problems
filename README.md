# Unscramble-Computer-Science-Problems

Solutions to a collection of five tasks based on a fabricated set of calls and texts. The efficiency of the solutions with run-time analyses are discussed below.

## Efficiency Analysis
An efficiency analysis based on time complexity for the solutions are performed below. 
### Task 0

> What is the first record of texts and what is the last record of calls?
>
>Print messages:
"First record of texts, \<incoming number> texts \<answering number> at time \<time>"
"Last record of calls, \<incoming number> calls \<answering number> at time \<time>, lasting \<during> seconds"

#### Analysis

- This task is achieved by array access.
- The complexity is O(1).

### Task 1

>How many different telephone numbers are there in the records? 
>
>Print a message:
"There are \<count> different telephone numbers in the records."

#### Analysis
- get_column function circulates an array once and it's O(n).
- get_unique converts a list to a set object. This conversion iterates over each
element and adds it to a hash map. Therefore the average and worst-case complexities
are O(n) and O(n**2), respectively. Since hash-collusions almost never happen, we can
safely assume O(n).
- get_unique_multi initially collects all numbers using a nested loop. 
The looped variables are irrelevant to the complexity. It, then, calls
get_column and get_unique subsequently. Subsequent calls do not increase
the complexity asymptotically. Therefore it's O(n).

- All in all, the task scales linearly w.r.t the size of the records. 


### Task 2

>Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
>
>Print a message:
"\<telephone number> spent the longest time, \<total time> seconds, on the phone during 
September 2016.".
#### Analysis
- add_to_dict is dictionary access, so O(1)
- get_longest_time does a forward pass in calls, which is O(n). 
  inner for loop is O(1). Then, in Line 37, max()'s complexity is O(n) as it does a single forward pass.
  Line 38 is dict access which is O(1). 

- Overall complexity is O(n).

### Task 3

>(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)
>
>Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
> - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
> - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
> - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.
>
>Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 \<list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
>
>Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?
>
>Print the answer as a part of a message::
"\<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits

#### Analysis
##### PART A:
- get_unique is O(n) (See Task 2).
- get_column is O(n) (See Task 1).
- get_prefix_type determines a number's prefix type that can be either fixed, mobile or telemarket.
  the complexities are O(n), O(1) and O(1) for fixed, mobile and telemarket checks, respectively.

- get_mobile_prefix runs get_prefix_type to determine the prefix type. 
  Then, it extracts the prefix based on the type's characteristic 
  given in the problem's description. 
  The complexities for extractions are O(n), O(1) and O(1) for fixed, mobile and telemarket,
  respectively. In mobile and telemarket types, we have fixed access. In fixed type, we have
  a search for ")" which is O(n). Then, we have slice access which depends on the index of ")", which is O(k). 
  Therefore, the function's complexity is O(n).

- get_numbers_called_from_area does one forward pass and checks with O(1) at each iteration. 
  Therefore O(n).
  
- For functions get_prefix_type and get_mobile_prefix, the numbers can be assumed to be fixed in length. 
  Therefore, even though these functions are O(n) w.r.t number length, the number lengths almost
  never change in length. In every part of the world, it is 10-15 characters long.
  Therefore, the complexities of these functions reduce to O(1),
  considering the input of our problem, which is the rows of our records.

- All in all, the complexity is O(n) + O(n) + O(n log n) as it uses timsort in its backend [1]. Complete complexity is O(n logn).

##### PART B:
- get_indices_of_same_area is O(n) due to a forward pass.
- calc_same_area_percentage is a sequence of O(n), O(n) and O(n) (Line 134-136).
  Percetange calculation is O(1)
- All in all it's O(n).


### Task 4

>A telephone company wants to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.
>
>Print a message:
"These numbers could be telemarketers: "
\<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.

#### Analysis
- get_possible_telemarketers adds numbers to sets with two subsequent for loops.
  Addition to Set is O(1) for each element and O(n) for the whole array.
  Moreover, the set substraction is O(n).   

- All in all, we have three O(n) subsequently, which makes the complexity O(n).



## References

\[1]: https://stackoverflow.com/questions/14434490/what-is-the-complexity-of-the-sorted-function




## Acknowledgements
This project is developed as a part of Data Structures and Algorithms course offered at Udacity. 