from algos.sorting import ASCENDING, SORTING_OPERATORS


def quick_sort(arr, order=ASCENDING, low=0, high=None):
    # TODO: error handling, validation of order; ASC or DESC
    length = len(arr)
    high = length - 1 if high is None else high

    if low < high:
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            # if current element is smaller than or equal to pivot
            if SORTING_OPERATORS[order.lower()](pivot, arr[j]) or pivot == arr[j]:
                # increment index of smaller element
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]

        # arr[partitioning_index] is now at right place
        partitioning_index = i + 1

        # separately sort elements before partition and after partition
        quick_sort(arr, order=order, low=low, high=partitioning_index - 1)
        quick_sort(arr, order=order, low=partitioning_index + 1, high=high)
    return arr
