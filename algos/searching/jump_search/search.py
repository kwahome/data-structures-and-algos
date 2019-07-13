import math

from algos import STRATEGIES
from algos.searching import UNSUCCESSFUL


def ijump_search(arr, target):
    """Iterative implementation of jump search.

    :param arr: input list
    :param target: search item
    :return: index of item if found `-1` otherwise
    """
    result = UNSUCCESSFUL
    length = len(arr)

    #: finding grid size to be jumped
    step = math.sqrt(length)

    #: finding the grid where element is present (if it's present)
    start = 0
    while arr[int(min(step, length) - 1)] < target and start < length:
        start = step
        step += math.sqrt(length)
        if start >= length:
            result = UNSUCCESSFUL
            break

    start = int(start)
    if start < length:
        #: doing a linear search for target in grid beginning with `start`.
        while arr[start] < target:
            start += 1

            #: if we reached next grid or end of array, element is not present.
            if start == min(step, length):
                result = UNSUCCESSFUL
                break

        #: if element is found
        if arr[start] == target:
            result = start
    return result


def rjump_search(arr, target, start=0, end=None):
    """Recursive implementation of jump search.

    :param arr: input list
    :param target: search item
    :param start: left most item in the search grid; it's start
    :param end: right most item in the search grid; it's end
    :return: index of item if found `-1` otherwise
    """
    result = UNSUCCESSFUL
    length = len(arr)

    end = length if end is None else end

    #: finding grid size to be jumped
    step = math.sqrt(end)

    #: finding the grid where element is present (if it's present)
    while arr[int(min(start + step, end) - 1)] < target and start < end:
        start += step
        step += math.sqrt(end)
        if start >= end:
            result = UNSUCCESSFUL
            break

    start = int(start)
    if start <= end - 1:
        #: element is found
        if arr[start] == target:
            result = start
        elif arr[start] < target:
            #: recursively jump search for target in grid between `start` and `end`
            result = rjump_search(arr, target, start=start + 1, end=end)
        elif arr[start] > target:
            #: recursively jump search for target in grid between `start` and `end`
            result = rjump_search(arr, target, start=start + 1, end=end - 1)
    return result


STRATEGY_MAP = {
    STRATEGIES.ITERATIVE: ijump_search,
    STRATEGIES.RECURSIVE: rjump_search
}


def jump_search(arr, target, strategy=STRATEGIES.ITERATIVE):
    return STRATEGY_MAP.get(strategy, ijump_search)(arr, target)
