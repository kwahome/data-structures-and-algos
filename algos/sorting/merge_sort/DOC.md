# Merge Sort
Merge sort is a sorting algorithm based on divide and conquer technique.

With worst-case time complexity being Ο(n log n), it is one of the most
respected algorithms.

Merge sort keeps on dividing the list into equal halves until it can no
more be divided.

By definition, if it is only one element in the list, it is sorted.
Then, merge sort combines the smaller sorted lists keeping the new
list sorted too.

# Algorithm:

	Step 1 − if it is only one element in the list it is already sorted, return.
	Step 2 − divide the list recursively into two halves until it can no more be divided.
	Step 3 − merge the smaller lists into new list in sorted order.


# Pseudocode:
```

	procedure mergesort( var a as array )
		if ( n == 1 ) return a

		var l1 as array = a[0] ... a[n/2]
		var l2 as array = a[n/2+1] ... a[n]

		l1 = mergesort( l1 )
		l2 = mergesort( l2 )

		return merge( l1, l2 )
	end procedure

	procedure merge( var a as array, var b as array )

		var c as array

		while ( a and b have elements )
	  		if ( a[0] > b[0] )
	     		add b[0] to the end of c
	     		remove b[0] from b
	  		else
	     		add a[0] to the end of c
	     		remove a[0] from a
	  		end if
		end while

		while ( a has elements )
	  		add a[0] to the end of c
	  		remove a[0] from a
		end while

		while ( b has elements )
	  		add b[0] to the end of c
	  		remove b[0] from b
		end while

		return c

	end procedure
```
