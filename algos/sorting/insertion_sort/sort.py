from algos import STRATEGIES
from algos.sorting import ASCENDING, GREATER_THAN, SORTING_OPERATORS


def iinsertion_sort(arr, order=ASCENDING):
    """Iterative implementation of insertion sort.

    :param arr: input list
    :param order: sorting order i.e "asc" or "desc"
    :return: list sorted in the order defined
    """
    operator = SORTING_OPERATORS.get(order.lower(), GREATER_THAN)
    for i in range(1, len(arr)):
        position = i - 1
        value = arr[i]
        while position >= 0 and operator(arr[position], value):
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = value
    return arr


def rinsertion_sort(arr, order=ASCENDING, position=1):
    """Recursive implementation of heap sort.

    :param arr: input list
    :param order: sorting order i.e "asc" or "desc"
    :param position: sorting position
    :return: list sorted in the order defined
    """
    value = arr[position]
    operator = SORTING_OPERATORS.get(order.lower(), GREATER_THAN)
    while position > 0 and operator(arr[position - 1], value):
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
    return STRATEGY_MAP.get(strategy, insertion_sort)(arr=arr, order=order)
