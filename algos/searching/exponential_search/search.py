from algos import STRATEGIES
from algos.searching.binary_search.search import binary_search


def exponential_search(arr, target, strategy=STRATEGIES.ITERATIVE):
    """Implementation of exponential search.

    :param arr: input list
    :param target: search item
    :param strategy: search strategy i.e "iterative" or "recursive"
    :return: index of item if found `-1` otherwise
    """
    length = len(arr)

    #: find range for binary search j by repeated doubling
    i = 1
    while i < length and arr[i] <= target:
        i = i * 2
    #: call binary search for the found range
    return binary_search(arr, target=target, left=i//2, right=min(i, length - 1), strategy=strategy)

