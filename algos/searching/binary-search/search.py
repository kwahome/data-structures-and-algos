from algos.searching import UNSUCCESSFUL


# iterative
def ibinary_search(arr, target):
    length = len(arr)
    left, right = 0, length-1

    while left <= right:
        mid = left + (right - left)//2
        if arr[mid] < target:
            # focus on right subtree
            left = mid + 1
        elif arr[mid] > target:
            # focus on left subtree
            right = mid - 1
        else:
            return mid
    return UNSUCCESSFUL


# recursive
def rbinary_search(arr, target, left=0, right=None):
    right = len(arr) - 1 if right is None else right

    # Base condition (search space is exhausted)
    if left > right:
        return UNSUCCESSFUL

    mid = left + (right - left)//2

    if arr[mid] < target:
        # focus on right subtree
        result = rbinary_search(arr, target, mid+1, right)
    elif arr[mid] > target:
        # focus on left subtree
        result = rbinary_search(arr, target, left, mid-1)
    else:
        result = mid
    return result
