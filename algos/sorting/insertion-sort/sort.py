from algos.sorting import ASCENDING, SORTING_OPERATORS


def insertion_sort(arr, order=ASCENDING):
    # TODO: error handling, validation of order; ASC or DESC
    for i in range(1, len(arr)):
        position = i - 1
        value = arr[i]
        while position >= 0 and SORTING_OPERATORS[order.lower()](arr[position], value):
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = value
    return arr


