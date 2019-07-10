import operator

from algos.sorting import ASCENDING, DESCENDING


class HEAPS:
    MAX = "max"
    MIN = "min"


HEAP_OPERATORS = {
    HEAPS.MAX: operator.gt,
    HEAPS.MIN: operator.lt
}

HEAP_SORT_ORDERING = {
    ASCENDING: HEAPS.MAX,
    DESCENDING: HEAPS.MIN
}
