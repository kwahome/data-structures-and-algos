from algos.searching import UNSUCCESSFUL


def linear_search(arr, target):
    length = len(arr)
    for i in range(length):
        if arr[i] == target:
            return i
    return UNSUCCESSFUL
