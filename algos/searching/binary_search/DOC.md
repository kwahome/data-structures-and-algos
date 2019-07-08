# Binary Search
Binary search works on sorted arrays.

Binary search begins by comparing the middle element of the array with
the target value. If the target value matches the middle element, its
position in the array is returned. If the target value is less than or
greater than the middle element, the search continues in the lower or
upper half of the array, respectively, eliminating the other half from
consideration.

# Algorithm:
Given an array A of n elements with values or records A0 ... An−1,
sorted such that A0 ≤ ... ≤ An−1, and target value T, the following
subroutine uses binary search to find the index of T in A.

	Step 1 − Set L to 0 and R to n − 1.
    Step 2 − If L > R, the search terminates as unsuccessful.
    Step 3 − Set m (the position of the middle element) to the floor (the largest previous integer) of (L + R) / 2.
    Step 4 − If Am < T, set L to m + 1 and go to step 2.
    Step 5 − If Am > T, set R to m – 1 and go to step 2.
    Step 6 − Now Am = T, the search is done; return m.

# Pseudocode
```

```
