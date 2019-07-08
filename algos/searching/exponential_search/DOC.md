# Exponential Search
Exponential search is also known as doubling or galloping search.

It is used to in searching sorted, unbounded/infinite arrays. It finds a
range that the target value resides in and perform a binary search
within that range.

The complexity of Exponential Search Technique:

- Time Complexity: O(1) for the best case. O(log2 i) for average or
    worst case. Where i is the location where search key is present.
- Space Complexity: O(1)

# Algorithm:
Given an array A of n elements with values or records A0 ... An−1,
sorted such that A0 ≤ ... ≤ An−1, and target value T, the following
subroutine uses binary search to find the index of T in A.

	Step 1 − Jump the array 2^i elements at a time searching for the condition Array[2^(i-1)] < valueWanted < Array[2^i]. If 2^i is greater than the lenght of array, then set the upper bound to the length of the array.
	Step 2 - Do a binary search between Array[2^(i-1)] and Array[2^i]

# Pseudocode
```
Begin
   if start <= end then
      mid := start + (end - start) /2
      if array[mid] = key then
         return mid location
      if array[mid] > key then
         call binarySearch(array, mid+1, end, key)
      else when array[mid] < key then
         call binarySearch(array, start, mid-1, key)
   else
      return invalid location
End
```
