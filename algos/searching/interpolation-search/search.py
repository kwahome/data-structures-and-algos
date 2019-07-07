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

        # condition of target found
        if arr[position] == target:
            result = position
            break

        # if target is larger, target is in upper part
        if arr[position] < target:
            low = position + 1

            # if target is smaller, target is in lower part
        else:
            high = position - 1
    return result
