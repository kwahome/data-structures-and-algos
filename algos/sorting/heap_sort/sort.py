from algos import STRATEGIES
from algos.sorting import ASCENDING, GREATER_THAN, SORTING_OPERATORS
from algos.sorting.heap_sort import HEAPS, HEAP_OPERATORS, HEAP_SORT_ORDERING


def iheapify(arr, heap_type=HEAPS.MAX):
    """Iteratively build a heap of type `heap_type`
    """
    divisor = 2.0 # 2.0 due to negative division rounding down in py 2
    operator = HEAP_OPERATORS[heap_type]
    for item in range(len(arr)):
        # check status of child (smaller/bigger) in respect to parent
        parent = int((item - 1) / divisor)
        if operator(arr[item], arr[parent]):
            child = item

            #: swap child and parent until desired status is achieved
            #: max heap -> child is smaller than parent
            #: min heap -> child is bigger than parent
            parent = int((child - 1) / divisor)
            while operator(arr[child], arr[parent]):
                arr[child], arr[parent] = arr[parent], arr[child]
                child = parent
                parent = int((child - 1) / divisor)
    return arr


def iheap_sort(arr, order=ASCENDING):
    # TODO: error handling, validation of order; ASC or DESC
    length = len(arr)

    # build a max or min heap in respect of sorting order
    #: ascending -> max heap
    #: descending -> mean heap
    arr = iheapify(arr, heap_type=HEAP_SORT_ORDERING[order.lower()])
    operator = SORTING_OPERATORS.get(order.lower(), GREATER_THAN)

    for i in range(length - 1, 0, -1):

        # swap value of first indexed with last indexed
        arr[0], arr[i] = arr[i], arr[0]

        # maintaining heap property after each swap
        j = 0

        while True:
            index = 2 * j + 1

            # if left child is smaller than right child point index variable to right child
            if index < (i - 1) and operator(arr[index + 1], arr[index]):
                index += 1

            # if parent is smaller than child, swap parent with child having higher value
            if index < i and operator(arr[index], arr[j]):
                arr[j], arr[index] = arr[index], arr[j]

            j = index
            if index >= i:
                break
    return arr


def rheapify(arr, length, root, heap_type=HEAPS.MAX):
    """Recursively heapify subtree rooted at root.
    """
    largest = root  # initialize largest as root
    left = 2 * root + 1  # left = 2 * i + 1
    right = 2 * root + 2  # right = 2 * i + 2

    operator = HEAP_OPERATORS[heap_type]

    # see if left child of root exists and is greater than root
    if left < length and operator(arr[left], arr[root]):
        largest = left

    # see if right child of root exists and is greater than root
    if right < length and operator(arr[right], arr[largest]):
        largest = right

    # change root, if needed
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]  # swap
        # heapify the root.
        rheapify(arr, length, largest, heap_type=heap_type)


def rheap_sort(arr, order=ASCENDING):
    # TODO: error handling, validation of order; ASC or DESC
    length = len(arr)

    heap_type = HEAP_SORT_ORDERING[order.lower()]

    # build a max or min heap based on the sorting order
    for i in range(length, -1, -1):
        rheapify(arr, length, i, heap_type=heap_type)

    # extract elements one at a time
    for i in range(length - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        rheapify(arr, i, 0, heap_type=heap_type)
    return arr


STRATEGY_MAP = {
    STRATEGIES.ITERATIVE: iheap_sort,
    STRATEGIES.RECURSIVE: rheap_sort
}


def heap_sort(arr, order=ASCENDING, strategy=STRATEGIES.ITERATIVE):
    return STRATEGY_MAP[strategy](arr=arr, order=order)
