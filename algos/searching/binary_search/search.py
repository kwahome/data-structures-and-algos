from algos import STRATEGIES
from algos.searching import UNSUCCESSFUL


def ibinary_search(arr, target, left=0, right=None):
    """Iterative implementation of binary search.

    :param arr: input list
    :param target: search item
    :param left: left most item in the search sub-array
    :param right: right most item in the search sub-array
    :return: index of item if found `-1` otherwise
    """
    right = len(arr) - 1 if right is None else right

    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] < target:
            #: focus on right sub-array
            left = mid + 1
        elif arr[mid] > target:
            #: focus on left sub-array
            right = mid - 1
        else:
            return mid
    return UNSUCCESSFUL


def rbinary_search(arr, target, left=0, right=None):
    """Recursive implementation of binary search.

    :param arr: input list
    :param target: search item
    :param left: left most item in the search sub-array
    :param right: right most item in the search sub-array
    :return: index of item if found `-1` otherwise
    """
    right = len(arr) - 1 if right is None else right

    #: base condition (search space is exhausted)
    if left > right:
        return UNSUCCESSFUL

    mid = left + (right - left)//2

    if arr[mid] < target:
        #: focus on right subtree
        result = rbinary_search(arr, target, mid+1, right)
    elif arr[mid] > target:
        #: focus on left subtree
        result = rbinary_search(arr, target, left, mid-1)
    else:
        result = mid
    return result


STRATEGY_MAP = {
    STRATEGIES.ITERATIVE: ibinary_search,
    STRATEGIES.RECURSIVE: rbinary_search
}


def binary_search(arr, target, left=0, right=None, strategy=STRATEGIES.ITERATIVE):
    return STRATEGY_MAP.get(strategy, ibinary_search)(arr, target, left, right)
