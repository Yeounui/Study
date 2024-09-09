import doctest

def findInSortedTabel(matrix, x):
    """
    >>> findInSortedTabel([[0, 2], [2, 4]], 2)
    True
    >>> findInSortedTabel([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]], 7)
    True
    >>> findInSortedTabel([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]], 4)
    True
    >>> findInSortedTabel([[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]], 8)
    False
    >>> findInSortedTabel([], 8)
    False
    """

    # Bring all elements into a set
    element_set = set()
    for row in matrix:
        element_set.update(row)

    # Return Boolean whether x is in the element set.
    return bool(x in element_set)

