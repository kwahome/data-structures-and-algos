# test cases
import operator

ASCENDING = "asc"
DESCENDING = "desc"

GREATER_THAN = operator.gt
LESS_THAN = operator.lt


SORTING_OPERATORS = {
    ASCENDING: GREATER_THAN,
    DESCENDING: LESS_THAN
}

TEST_CASES = (
    #: (INPUT, EXPECTED OUTPUT, ORDER)
    (
        [20, 3, -5, 50, 1, 9, 5, -2, 30, 13],
        [-5, -2, 1, 3, 5, 9, 13, 20, 30, 50],
        ASCENDING
    ),
    (
        [20, 3, -5, 50, 1, 9, 5, -2, 30, 13],
        [50, 30, 20, 13, 9, 5, 3, 1, -2, -5],
        DESCENDING
    ),
    (
        ["a", "z", "f", "b", "k", "r", "i", "v", "e", "m"],
        ["a", "b", "e", "f", "i", "k", "m", "r", "v", "z"],
        ASCENDING
    ),
    (
        ["a", "z", "f", "b", "k", "r", "i", "v", "e", "m"],
        ["z", "v", "r", "m", "k", "i", "f", "e", "b", "a"],
        DESCENDING
    ),
)
