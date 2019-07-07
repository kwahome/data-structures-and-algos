from algos.searching import UNSUCCESSFUL


def interpolation_search(arr, target):
    result = UNSUCCESSFUL
    length = len(arr)

    # find indexes of two corners
    low = 0
    high = (length - 1)

    # since array is sorted, an element present in array must be in range defined by corner
    while low <= high and arr[high] >= target >= arr[low]:
        if low == high:
            if arr[low] == target:
                result = low
            break

        # probing the position with keeping uniform distribution in mind.
        position = low + int(((float(high - low) / (arr[high] - arr[low])) * (target - arr[low])))

        if arr[position] == target:
            # target found
            result = position
            break

        if arr[position] < target:
            # if target is larger, target is in upper part
            low = position + 1
        else:
            # if target is smaller, target is in lower part
            high = position - 1
    return result
