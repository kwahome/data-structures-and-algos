from algos.sorting import ASCENDING, SORTING_OPERATORS


def merge_sort(arr, order=ASCENDING):
    # TODO: error handling, validation of order; ASC or DESC
    length = len(arr)
    if length > 1:
        mid = length // 2  # ceiling

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left, order=order)
        merge_sort(right, order=order)

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if SORTING_OPERATORS[order.lower()](left[i], right[j]):
                arr[k] = right[j]
                j += 1
            else:
                arr[k] = left[i]
                i += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
