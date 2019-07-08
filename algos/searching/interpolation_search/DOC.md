# Interpolation Search
Interpolation search is an improved variant of binary search.

This search algorithm works on the probing position of the required
value.

For this algorithm to work properly, the data collection should be in a
sorted form and equally distributed.

There are cases where the location of target data may be known in
advance. For example, in case of a telephone directory, if we want to
search the telephone number of Morphius.

Here, linear search and even binary search will seem slow as we can
directly jump to memory space where the names start from 'M' are stored.

# Algorithm:
Interpolation search finds a particular item by computing the probe
position.

Initially, the probe position is the position of the middle most item of
the collection.

If a match occurs, then the index of the item is returned.
To split the list into two parts, we use the following method:

	mid = Lo + ((Hi - Lo) / (A[Hi] - A[Lo])) * (X - A[Lo])

	where −
   	A    = list
   	Lo   = Lowest index of the list
   	Hi   = Highest index of the list
   	A[n] = Value stored at index n in the list

If the middle item is greater than the item, then the probe position is
again calculated in the sub-array to the right of the middle item.
Otherwise, the item is searched in the subarray to the left of the
middle item. This process continues on the sub-array as well until the
size of subarray reduces to zero.

Runtime complexity of interpolation search algorithm is Ο(log (log n))
as compared to Ο(log n) of BST in favorable situations.

	Step 1 − Start searching data from middle of the list.
	Step 2 − If it is a match, return the index of the item, and exit.
	Step 3 − If it is not a match, probe position.
	Step 4 − Divide the list using probing formula and find the new midle.
	Step 5 − If data is greater than middle, search in higher sub-list.
	Step 6 − If data is smaller than middle, search in lower sub-list.
	Step 7 − Repeat until match.

# Pseudocode
```

```
