from algos import STRATEGIES
from algos.sorting import ASCENDING, GREATER_THAN, SORTING_OPERATORS


def ibubble_sort(arr, order=ASCENDING):
    operator = SORTING_OPERATORS.get(order.lower(), GREATER_THAN)
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if operator(arr[j], arr[j + 1]):
                # swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def rbubble_sort(arr, order=ASCENDING):
    operator = SORTING_OPERATORS.get(order.lower(), GREATER_THAN)
    for i in range(len(arr) - 1):
        if operator(arr[i], arr[i + 1]):
            # perform first run then recurse
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            rbubble_sort(arr, order=order)
    return arr


STRATEGY_MAP = {
    STRATEGIES.ITERATIVE: ibubble_sort,
    STRATEGIES.RECURSIVE: rbubble_sort
}


def bubble_sort(arr, order=ASCENDING, strategy=STRATEGIES.ITERATIVE):
    return STRATEGY_MAP.get(strategy, STRATEGIES.ITERATIVE)(arr=arr, order=order)
