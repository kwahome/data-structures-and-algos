# Radix Sort
Radix sort is a non-comparative integer sorting algorithm that sorts
data with integer keys by grouping keys by the individual digits which
share the same significant position and value.

A positional notation is required, but because integers can represent
strings of characters (e.g., names or dates) and specially formatted
floating point numbers, radix sort is not limited to integers.

The lower bound for Comparison based sorting algorithm (Merge Sort,
Heap Sort, Quick-Sort .. etc) is Ω(nLogn), i.e., they cannot do better
than nLogn.

The idea of Radix Sort is to do digit by digit sort starting from least
significant digit to most significant digit. Radix sort uses counting
sort as a subroutine to sort.

# Algorithm:

	Step 1 − Take the least significant digit (or group of bits, both being examples of radices) of each key.
	Step 2 − Group the keys based on that digit, but otherwise keep the original order of keys. (From the second step on this is required for the algorithm. If applied generally it makes the LSD radix sort a stable sort.)
	Step 3 − Collect the groups (buckets) in the order of the digits and repeat the grouping process with each more significant digit.


# Pseudocode:
```
```
