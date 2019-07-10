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

TEST_CASES = {
    "CASES": (
        # (INPUT, EXPECTED OUTPUT, ORDER)
        ([20, 3, -5, 50, 1, 9, 5, -2, 30, 13], [-5, -2, 1, 3, 5, 9, 13, 20, 30, 50], ASCENDING),
        ([20, 3, -5, 50, 1, 9, 5, -2, 30, 13], [50, 30, 20, 13, 9, 5, 3, 1, -2, -5], DESCENDING),

    )
}
