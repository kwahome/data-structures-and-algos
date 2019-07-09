from algos import STRATEGIES
from algos.sorting import ASCENDING, SORTING_OPERATORS


def imerge_sort(arr, order=ASCENDING):
    """In-place merge sort of array without recursion.
    The basic idea is to avoid the recursive call while using iterative solution.

    The algorithm first merge chunk of length of 2, then merge chunks of length 4, then 8, 16, ...,
    until 2^k where 2^k is large than the length of the array
    """

    # TODO: error handling, validation of order; ASC or DESC
    length = len(arr)

    unit = 1
    while unit <= length:
        for index in range(0, length, unit * 2):
            left, right = index, min(length, index + 2 * unit)
            mid = index + unit

            while left < mid < right:
                if SORTING_OPERATORS[order.lower()](arr[mid], arr[left]):
                    left += 1
                else:
                    tmp = arr[mid]
                    arr[left + 1: mid + 1] = arr[left:mid]
                    arr[left] = tmp
                    left, mid, mid = left + 1, mid + 1, mid + 1
        unit *= 2
    return arr


def rmerge_sort(arr, order=ASCENDING):
    # TODO: error handling, validation of order; ASC or DESC
    length = len(arr)
    if length > 1:
        mid = length // 2  # ceiling

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, order=order)
        merge_sort(right, order=order)

        i = j = k = 0

        # copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if SORTING_OPERATORS[order.lower()](left[i], right[j]):
                arr[k] = right[j]
                j += 1
            else:
                arr[k] = left[i]
                i += 1
            k += 1

        # checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


STRATEGY_MAP = {
    STRATEGIES.ITERATIVE: imerge_sort,
    STRATEGIES.RECURSIVE: rmerge_sort
}


def merge_sort(arr, order=ASCENDING, strategy=STRATEGIES.ITERATIVE):
    return STRATEGY_MAP[strategy](arr=arr, order=order)
