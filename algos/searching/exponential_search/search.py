from algos.searching.binary_search.search import binary_search


# iterative
def exponential_search(arr, target):
    length = len(arr)

    # if target is present at first  location itself
    if arr[0] == target:
        return 0

    # find range for binary search j by repeated doubling
    i = 1
    while i < length and arr[i] <= target:
        i = i * 2
    # call binary search for the found range
    return binary_search(arr, target=target, left=i//2, right=min(i, length - 1))

