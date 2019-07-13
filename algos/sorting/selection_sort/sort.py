from algos import STRATEGIES
from algos.sorting import ASCENDING, GREATER_THAN, SORTING_OPERATORS


def iselection_sort(arr, order=ASCENDING):
    """Iterative implementation of quick sort.

    :param arr: input list
    :param order: sorting order i.e "asc" or "desc"
    :return: list sorted in the order defined
    """
    length = len(arr)
    operator = SORTING_OPERATORS.get(order.lower(), GREATER_THAN)
    for i in range(length):
        #: mark the min/max (depending on order) index
        #: then look for the min/max in the remaining unsorted array and swap
        index = i
        for j in range(i+1, length):
            if operator(arr[index], arr[j]):
                index = j
        arr[i], arr[index] = arr[index], arr[i]
    return arr


def rselection_sort(arr, order=ASCENDING, position=0, minimum=1, ):
    """Recursive implementation of quick sort.

    :param arr: input list
    :param order: sorting order i.e "asc" or "desc"
    :param position: sorting position
    :param minimum: minimum item
    :return: list sorted in the order defined
    """
    length = len(arr)
    operator = SORTING_OPERATORS.get(order.lower(), GREATER_THAN)
    if position < length - 1:
        if minimum < length:
            #: swap when index and minimum index are not same
            if operator(arr[position], arr[minimum]):
                arr[minimum], arr[position] = arr[position], arr[minimum]
            rselection_sort(arr, order=order, position=position, minimum=minimum + 1)
        else:
            rselection_sort(arr, order=order, position=position + 1, minimum=position + 1)
    return arr


STRATEGY_MAP = {
    STRATEGIES.ITERATIVE: iselection_sort,
    STRATEGIES.RECURSIVE: rselection_sort
}


def selection_sort(arr, order=ASCENDING, strategy=STRATEGIES.ITERATIVE):
    return STRATEGY_MAP.get(strategy, iselection_sort)(arr=arr, order=order)
