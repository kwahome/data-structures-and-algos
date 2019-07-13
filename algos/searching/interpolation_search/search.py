from algos import STRATEGIES
from algos.searching import UNSUCCESSFUL


def iinterpolation_search(arr, target):
    """Iterative implementation of interpolation search.

    :param arr: input list
    :param target: search item
    :return: index of item if found `-1` otherwise
    """
    result = UNSUCCESSFUL
    length = len(arr)

    #: find indexes of two corners
    low = 0
    high = (length - 1)

    #: since array is sorted, an element present in array must be in range defined by corner
    while low <= high and arr[high] >= target >= arr[low]:
        if low == high:
            if arr[low] == target:
                result = low
            break

        #: probing the position with keeping uniform distribution in mind.
        position = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))

        if arr[position] == target:
            #: target found
            result = position
            break

        if arr[position] < target:
            #: if target is larger, target is in upper part
            low = position + 1
        else:
            #: if target is smaller, target is in lower part
            high = position - 1
    return result


def rinterpolation_search(arr, target, low=0, high=None):
    """Recursive implementation of interpolation search.

    :param arr: input list
    :param target: search item
    :param low: left most item
    :param high: right most item
    :return: index of item if found `-1` otherwise
    """
    result = UNSUCCESSFUL
    length = len(arr)

    #: find indexes of two corners
    high = length - 1 if high is None else high

    if low <= high:
        #: probing the position with keeping uniform distribution in mind.
        position = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))

        #: check position is not out of range
        if position < length:
            #: if target is larger, target is in upper part
            if arr[position] < target:
                result = rinterpolation_search(arr, target, low=position + 1, high=high)

            #: if target is smaller, target is in lower part
            elif arr[position] > target:
                result = rinterpolation_search(arr, target, low=low, high=position - 1)

            #: target found
            else:
                result = position
    return result


STRATEGY_MAP = {
    STRATEGIES.ITERATIVE: iinterpolation_search,
    STRATEGIES.RECURSIVE: rinterpolation_search
}


def interpolation_search(arr, target, strategy=STRATEGIES.ITERATIVE):
    return STRATEGY_MAP.get(strategy, iinterpolation_search)(arr, target)
