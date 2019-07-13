from algos import STRATEGIES
from algos.sorting import ASCENDING, GREATER_THAN, SORTING_OPERATORS


def imerge_sort(arr, order=ASCENDING):
    """Iterative implementation of merge sort.

    The basic idea is to avoid the recursive call by using iteration to sort.
    The algorithm first merge chunk of length of 2, then merge chunks of length 4,
    then 8, 16, ..., until 2^k where 2^k is large than the length of the array

    :param arr: input list
    :param order: sorting order i.e "asc" or "desc"
    :return: list sorted in the order defined
    """
    length = len(arr)
    operator = SORTING_OPERATORS.get(order.lower(), GREATER_THAN)
    position = 1
    while position <= length:
        for index in range(0, length, position * 2):
            left, right = index, min(length, index + 2 * position)
            mid = index + position

            while left < mid < right:
                if operator(arr[mid], arr[left]):
                    left += 1
                else:
                    value = arr[mid]
                    arr[left + 1: mid + 1] = arr[left:mid]
                    arr[left] = value
                    left, mid = left + 1, mid + 1
        position *= 2
    return arr


def rmerge_sort(arr, order=ASCENDING):
    """Recursive implementation of merge sort.

    :param arr: input list
    :param order: sorting order i.e "asc" or "desc"
    :return: list sorted in the order defined
    """
    length = len(arr)
    operator = SORTING_OPERATORS.get(order.lower(), GREATER_THAN)
    if length > 1:
        mid = length // 2  #: ceiling
        left, right = arr[:mid], arr[mid:]

        rmerge_sort(left, order=order)
        rmerge_sort(right, order=order)

        i = j = k = 0

        #: copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if operator(left[i], right[j]):
                arr[k] = right[j]
                j += 1
            else:
                arr[k] = left[i]
                i += 1
            k += 1

        #: checking if any element was left in the left sub-array
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        #: checking if any element was left in the right sub-array
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
    return STRATEGY_MAP.get(strategy, imerge_sort)(arr=arr, order=order)
