# Quick Sort
Quick sort is a highly efficient sorting algorithm and is based on
partitioning of array of data into smaller arrays.

Quick sort partitions an array and then calls itself recursively twice
to sort the two resulting sub-arrays.

A large array is partitioned into two arrays one of which holds values
smaller than the specified value, say pivot, based on which the
partition is made and another array holds values greater than the pivot
value.

This algorithm is quite efficient for large-sized data sets as its
average and worst case complexity are of Ο(n2), where n is the number
of items.

# Algorithm:

	Step 1 − Make the right-most index value pivot
	Step 2 − partition the array using pivot value
	Step 3 − quicksort left partition recursively
	Step 4 − quicksort right partition recursively


# Pseudocode
```
procedure quickSort(left, right)

    if right-left <= 0
        return
    else
        pivot = A[right]
        partition = partitionFunc(left, right, pivot)
        quickSort(left,partition-1)
        quickSort(partition+1,right)
    end if

end procedure
```
