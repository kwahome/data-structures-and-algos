# Bubble Sort
Bubble sort is an simple elementary sorting algorithm.

This sorting algorithm is comparison-based algorithm in which each pair
of adjacent elements is compared and the elements are swapped if they
are not in order.

The idea is to imagine bubbling the smallest elements of a (vertical)
array to the top; then bubble the next smallest; then so on until the
entire array is sorted.

Bubble sort is worse than both insertion sort and selection sort.
It moves elements as many times as insertion sort (bad) and it takes as
long as selection sort (bad).

On the positive side, bubble sort is easy to understand. Also there are
highly improved variants of bubble sort.


It is not suitable for large data sets as its average and worst case
complexity are of Ο(n2) where n is the number of items.

# Algorithm:
We assume list is an array of n elements.
We further assume that swap function swaps the values of the given array
elements.

Bubble sort follows the steps below:

	Step 1 − For each element at index i from n to 0, loop:
    Step 2 − For each element at index j, from n to i exclusive, loop
    Step 3 − If the element at j is less than that at j+1, do swap

# Pseudocode
```
begin BubbleSort(list)
   for all elements of list
      if list[i] > list[i+1]
         swap(list[i], list[i+1])
      end if
   end for
   return list
end BubbleSort
```
