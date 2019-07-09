# Jump Search
Like Binary Search, Jump Search is a searching algorithm for sorted
arrays. The basic idea is to check fewer elements (than linear search)
by jumping ahead by fixed steps or skipping some elements in place of
searching all elements.

For example, suppose we have an array arr[] of size n and block (to be
jumped) size m. Then we search at the indexes arr[0], arr[m],
arr[2m]…..arr[km] and so on. Once we find the interval
(arr[km] < x < arr[(k+1)m]), we perform a linear search operation from
the index km to find the element x..

# Algorithm:
Let’s consider the following array:
(0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610). Length of
the array is 16. Jump search will find the value of 55 with the
following steps assuming that the block size to be jumped is 4.

	Step 1 − Jump from index 0 to index 4;
    Step 2 − Jump from index 4 to index 8;
    Step 3 − Jump from index 8 to index 12;
    Step 4 − Since the element at index 12 is greater than 55 we will jump back a step to come to index 9.
    Step 5 - Perform linear search from index 9 to get the element 55.

# Pseudocode
```
Begin JumpSearch
  Input: An ordered list L, its length n and a search key s.
  Output: The position of s in L, or nothing if s is not in L.

  a ← 0
  b ← ⌊√n⌋

  while Lmin(b,n)-1 < s do
    a ← b
    b ← b + ⌊√n⌋
    if a ≥ n then
      return nothing

  while La < s do
    a ← a + 1
    if a = min(b,n)
      return nothing

  if La = s then
    return a
  else
    return nothing
End JumpSearch
```
