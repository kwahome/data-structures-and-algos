from algos.sorting import ASCENDING, GREATER_THAN, SORTING_OPERATORS


def selection_sort(arr, order=ASCENDING):
    length = len(arr)
    operator = SORTING_OPERATORS.get(order.lower(), GREATER_THAN)
    for i in range(length):
        # mark the min/max (depending on order) index
        # then look for the min/max in the remaining unsorted array and swap
        index = i
        for j in range(i+1, length):
            if operator(arr[index], arr[j]):
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr
