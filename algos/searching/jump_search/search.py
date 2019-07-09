import math
from algos.searching import UNSUCCESSFUL


def jump_search(arr, target):
    result = UNSUCCESSFUL
    length = len(arr)

    # finding block size to be jumped
    step = math.sqrt(length)

    # finding the block where element is present (if it's present)
    previous = 0
    while arr[int(min(step, length) - 1)] < target:
        previous = step
        step += math.sqrt(length)
        if previous >= length:
            result = UNSUCCESSFUL
            break

    previous = int(previous)

    if previous <= length:
        # doing a linear search for target in block beginning with previous.
        while arr[previous] < target:
            previous += 1

            # if we reached next block or end of array, element is not present.
            if previous == min(step, length):
                result = UNSUCCESSFUL
                break

        # if element is found
        if arr[previous] == target:
            result = previous
    return result
