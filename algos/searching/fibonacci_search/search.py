from algos.searching import UNSUCCESSFUL


def fibonacci_search(arr, target):
    result = UNSUCCESSFUL
    length = len(arr)

    # initialize fibonacci numbers
    fib_m2 = 0  # (m-2)'th Fibonacci No.
    fib_m1 = 1  # (m-1)'th Fibonacci No.
    fib_m = fib_m2 + fib_m1  # m'th Fibonacci

    # fib_m is going to store the smallest fibonacci number greater than or equal to length
    while fib_m < length:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    # marks the eliminated range from front
    offset = -1

    # while there are elements to be inspected.
    # note that we compare arr[fib_m] with x.
    # when fib_m becomes 1, fib_2 becomes 0
    while fib_m > 1:
        # check if fib_2 is a valid location
        i = min(offset + fib_m2, length - 1)
        # if target is greater than the value at index fib_2, slice the sub array from offset to i
        if arr[i] < target:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i

        # if target is greater than the value at index fib_2, slice the sub-array after i+1
        elif arr[i] > target:
            fib_m = fib_m2
            fib_m1 = fib_m1 - fib_m2
            fib_m2 = fib_m - fib_m1

            # element found. return index
        else:
            result = i
            break

    # comparing the last element with x */
    # last_index = offset + 1
    # if fib_m1 and arr[last_index] == target:
    #     return last_index
    return result
