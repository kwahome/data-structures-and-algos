from algos import STRATEGIES
from algos.sorting import ASCENDING, SORTING_OPERATORS


def ibubble_sort(arr, order=ASCENDING):
    # TODO: error handling, validation of order; ASC or DESC
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if SORTING_OPERATORS.get(order.lower())(arr[j], arr[j + 1]):
                # swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def rbubble_sort(arr, order=ASCENDING):
    # TODO: error handling, validation of order; ASC or DESC
    for i in range(len(arr) - 1):
        if SORTING_OPERATORS.get(order.lower())(arr[i], arr[i + 1]):
            # perform first run then recurse
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            rbubble_sort(arr, order=order)
    return arr


STRATEGY_MAP = {
    STRATEGIES.ITERATIVE: ibubble_sort,
    STRATEGIES.RECURSIVE: rbubble_sort
}


def bubble_sort(arr, order=ASCENDING, strategy=STRATEGIES.ITERATIVE):
    return STRATEGY_MAP[strategy](arr=arr, order=order)
