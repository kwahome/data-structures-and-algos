from algos.sorting import ASCENDING, SORTING_OPERATORS


def bubble_sort(arr, order=ASCENDING):
    # TODO: error handling, validation of order; ASC or DESC
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if SORTING_OPERATORS.get(order.lower())(arr[j], arr[j + 1]):
                # swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
