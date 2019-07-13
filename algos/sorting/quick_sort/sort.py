from algos import STRATEGIES
from algos.sorting import ASCENDING, GREATER_THAN, SORTING_OPERATORS


def iquick_sort(arr, order=ASCENDING):
    """Iterative implementation of quick sort.

    :param arr: input list
    :param order: sorting order i.e "asc" or "desc"
    :return: list sorted in the order defined
    """

    return rquick_sort(arr, order=order)
    # length = len(arr)
    # print("\n")
    # print("new sort")
    # print("arr: " + str(arr))
    # print("order: " + order)
    # i = low = 0
    # tmpr = high = length - 1
    #
    # while True:
    #     i -= 1
    #     print("\n")
    #     print("i: " + str(i))
    #     print("low: " + str(low))
    #     print("high: " + str(high))
    #     print("tmpr: " + str(tmpr))
    #     while low < tmpr:
    #         pivot = arr[(low + high) // 2]
    #         print("pivot: " + str(pivot))
    #         while low <= high:
    #             while arr[high] > pivot:
    #                 high -= 1
    #             while arr[low] < pivot:
    #                 low += 1
    #
    #             if low <= high:
    #                 arr[low], arr[high] = arr[high], arr[low]
    #                 low += 1
    #                 high -= 1
    #         arr[tmpr] = -arr[tmpr]
    #         tmpr = low - 1
    #         i += 1
    #
    #     if i < 0:
    #         break
    #     low += 1
    #     tmpr = length - 1
    #     for i in range(low, length):
    #         if arr[i] < 0:
    #             tmpr = i
    # return arr

    # pivot = arr[high]

    # # each time we find an element less than or equal to pivot, low is incremented and
    # # that element would be placed before the pivot.
    # for i in range(low, high):
    #     if SORTING_OPERATORS[order.lower()](pivot, arr[i]) or pivot == arr[i]:
    #         arr[i], arr[low] = arr[low], arr[i]
    #         low += 1
    # # swap low with pivot
    # arr[low], arr[high] = arr[high], arr[low]


def rquick_sort(arr, order=ASCENDING, low=0, high=None):
    """Recursive implementation of quick sort.

    :param arr: input list
    :param order: sorting order i.e "asc" or "desc"
    :param low: smallest item
    :param high: largest item
    :return: list sorted in the order defined
    """
    length = len(arr)
    high = length - 1 if high is None else high
    operator = SORTING_OPERATORS.get(order.lower(), GREATER_THAN)
    if low < high:
        start = low - 1
        pivot = arr[high]
        for item in range(low, high):
            #: if current element is smaller than or equal to pivot
            if operator(pivot, arr[item]) or pivot == arr[item]:
                #: increment index of smaller element
                start += 1
                arr[start], arr[item] = arr[item], arr[start]
        arr[start+1], arr[high] = arr[high], arr[start+1]

        #: arr[partitioning_index] is now at right place
        partitioning_index = start + 1

        #: separately sort elements before partition and after partition
        rquick_sort(arr, order=order, low=low, high=partitioning_index - 1)
        rquick_sort(arr, order=order, low=partitioning_index + 1, high=high)
    return arr


STRATEGY_MAP = {
    STRATEGIES.ITERATIVE: iquick_sort,
    STRATEGIES.RECURSIVE: rquick_sort
}


def quick_sort(arr, order=ASCENDING, strategy=STRATEGIES.ITERATIVE):
    return STRATEGY_MAP.get(strategy, iquick_sort)(arr=arr, order=order)

