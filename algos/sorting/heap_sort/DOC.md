# Heap Sort
Heap sort is a comparison based sorting technique based on Binary Heap
data structure.

It can be thought of as an improved selection sort: like that algorithm,
it divides its input into a sorted and an unsorted region, and it
iteratively shrinks the unsorted region by extracting the largest
element and moving that to the sorted region. The improvement consists
of the use of a heap data structure rather than a linear-time search to
find the maximum.

Although somewhat slower in practice on most machines than a
well-implemented quicksort, it has the advantage of a more favorable
worst-case O(n log n) runtime. Heapsort is an in-place algorithm, but it
is not a stable sort.

# Algorithm:

	Step 1 − Call the buildMaxHeap() function on the list. Also referred to as heapify(), this builds a heap from a list in O(n) operations.
	Step 2 − Swap the first element of the list with the final element. Decrease the considered range of the list by one.
	Step 3 − Call the siftDown() function on the list to sift the new first element to its appropriate index in the heap.
	Step 4 − Go to step (2) unless the considered range of the list is one element.



# Pseudocode:
```
procedure heapsort(a, count) is
    input: an unordered array a of length count

    (Build the heap in array a so that largest value is at the root)
    heapify(a, count)

    (The following loop maintains the invariants that a[0:end] is a heap and every element
     beyond end is greater than everything before it (so a[end:count] is in sorted order))
    end ← count - 1
    while end > 0 do
        (a[0] is the root and largest value. The swap moves it in front of the sorted elements.)
        swap(a[end], a[0])
        (the heap size is reduced by one)
        end ← end - 1
        (the swap ruined the heap property, so restore it)
        siftDown(a, 0, end)
```
