from algos import STRATEGIES
from algos.sorting import ASCENDING, SORTING_OPERATORS


def iinsertion_sort(arr, order=ASCENDING):
    # TODO: error handling, validation of order; ASC or DESC
    for i in range(1, len(arr)):
        position = i - 1
        value = arr[i]
        while position >= 0 and SORTING_OPERATORS[order.lower()](arr[position], value):
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = value
    return arr


def rinsertion_sort(arr, order=ASCENDING, position=1):
    value = arr[position]

    while position > 0 and SORTING_OPERATORS[order.lower()](arr[position - 1], value):
        arr[position] = arr[position - 1]
        position -= 1
    arr[position] = value

    if position < len(arr) - 1:
        rinsertion_sort(arr, order=order, position=position + 1)
    return arr


STRATEGY_MAP = {
    STRATEGIES.ITERATIVE: iinsertion_sort,
    STRATEGIES.RECURSIVE: rinsertion_sort
}


def insertion_sort(arr, order=ASCENDING, strategy=STRATEGIES.ITERATIVE):
    return STRATEGY_MAP[strategy](arr=arr, order=order)
