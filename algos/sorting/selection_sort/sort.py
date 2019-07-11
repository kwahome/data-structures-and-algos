from algos import STRATEGIES
from algos.sorting import ASCENDING, GREATER_THAN, SORTING_OPERATORS


def iselection_sort(arr, order=ASCENDING):
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


def rselection_sort(arr, root=0, minor=1, order=ASCENDING):
    length = len(arr)
    operator = SORTING_OPERATORS.get(order.lower(), GREATER_THAN)
    if root < length - 1:
        if minor < length:
            # swap when index and minimum index are not same
            if operator(arr[root], arr[minor]):
                arr[minor], arr[root] = arr[root], arr[minor]
            rselection_sort(arr, root=root, minor=minor + 1, order=order)
        else:
            rselection_sort(arr, root=root + 1, minor=root + 1, order=order)
    return arr


STRATEGY_MAP = {
    STRATEGIES.ITERATIVE: iselection_sort,
    STRATEGIES.RECURSIVE: rselection_sort
}


def selection_sort(arr, order=ASCENDING, strategy=STRATEGIES.ITERATIVE):
    return STRATEGY_MAP.get(strategy, STRATEGIES.ITERATIVE)(arr=arr, order=order)
