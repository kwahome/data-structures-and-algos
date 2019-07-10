# Counting Sort
Counting sort is a sorting technique based on keys between a specific
range.

It works by counting the number of objects having distinct key values
(kind of hashing). Then doing some arithmetic to calculate the position
of each object in the output sequence.


# Algorithm:

	Step 1 − Take a count array to store the count of each unique object.
	Step 2 − Modify the count array such that each element at each index stores the sum of previous counts.
	Step 3 − Output each object from the input sequence followed by decreasing its count by 1.


# Pseudocode:
```
Begin countingSort(array, k) is
  count ← new array of k zeros
  for i = 1 to length(array) do
    count[array[i]] ← count[array[i]] + 1
  for i = 2 to k do
    count[i] ← count[i] + count[i - 1]
  for i = length(array) downto 1 do
    output[count[array[i]]] ← array[i]
    count[array[i]] ← count[array[i]] - 1
  return output
End countingSort
```
