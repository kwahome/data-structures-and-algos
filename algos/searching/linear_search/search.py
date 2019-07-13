from algos.searching import UNSUCCESSFUL


def linear_search(arr, target):
    """Implementation of linear search.

    :param arr: input list
    :param target: search item
    :return: index of item if found `-1` otherwise
    """
    length = len(arr)
    for i in range(length):
        if arr[i] == target:
            return i
    return UNSUCCESSFUL
