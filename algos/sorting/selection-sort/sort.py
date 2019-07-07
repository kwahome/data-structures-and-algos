from algos.sorting import ASCENDING, SORTING_OPERATORS


def selection_sort(arr, order=ASCENDING):
    # TODO: error handling, validation of order; ASC or DESC
    length = len(arr)
    for i in range(length):
        # mark the min/max (depending on order) index
        # then look for the min/max in the remaining unsorted array and swap
        index = i
        for j in range(i+1, length):
            if SORTING_OPERATORS[order.lower()](arr[index], arr[j]):
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr
