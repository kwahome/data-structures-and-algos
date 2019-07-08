# test cases
import operator

ASCENDING = "asc"
DESCENDING = "desc"
SORTING_OPERATORS = {
    ASCENDING: operator.gt,
    DESCENDING: operator.lt
}

TEST_CASES = {
    "UNSORTED": [20, 3, 50, 1, 9, 5, 30, 13],

    "SORTED": {
        ASCENDING: [1, 3, 5, 9, 13, 20, 30, 50],
        DESCENDING: [50, 30, 20, 13, 9, 5, 3, 1]
    },

    "UNSORTED_ARRAY": [20, 3, 50, 1, 9, 5, 30, 13],
    "CASES": (
        # (INPUT, EXPECTED OUTPUT, ORDER)
        ([20, 3, 50, 1, 9, 5, 30, 13], [1, 3, 5, 9, 13, 20, 30, 50], ASCENDING),
        ([20, 3, 50, 1, 9, 5, 30, 13], [50, 30, 20, 13, 9, 5, 3, 1], DESCENDING),

    )
}
