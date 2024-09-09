def flip(pancakes, burnt = False):
    """
    >>> flip((9, 2, 7, 5, 8, 1, 4, 6, 3))
    (3, 6, 4, 1, 8, 5, 7, 2, 9)
    >>> flip((-9, -2, -7, 5, 8, -1, -4, -6, 3), burnt=True)
    (-3, 6, 4, 1, -8, -5, 7, 2, 9)
    """
    flipped = pancakes[::-1]
    if burnt:
        flipped = [-pancake for pancake in flipped]
        if not isinstance(flipped, type(pancakes)):
            flipped = tuple(flipped)
    return flipped

def flip_top(pancakes, flipBase, burnt = False):
    """
    >>> flip_top((1, 4, 6, 3, 5, 2, 7, 8, 9), 3)
    (6, 4, 1, 3, 5, 2, 7, 8, 9)
    >>> flip_top((6, 4, 1, 3, 5, 2, 7, 8, 9), 6)
    (2, 5, 3, 1, 4, 6, 7, 8, 9)
    >>> flip_top((-1, -4, -6, 3, -5, -2, 7, 8, 9), 3, burnt=True)
    (6, 4, 1, 3, -5, -2, 7, 8, 9)
    >>> flip_top((6, 4, 1, 3, -5, -2, 7, 8, 9), 1, burnt=True)
    (-6, 4, 1, 3, -5, -2, 7, 8, 9)
    >>> flip_top((-6, 4, 1, 3, -5, -2, 7, 8, 9), 6, burnt=True)
    (2, 5, -3, -1, -4, 6, 7, 8, 9)
    """
    flipped = flip(pancakes[:flipBase], burnt)
    return flipped + pancakes[flipBase:]

def find_largest(pancakes, flipBase):
    """
    >>> find_largest((1, 4, 6, 3, 5, 2, 7, 8, 9), 6)
    3
    >>> find_largest((-1, -4, -6, 3, -5, -2, 7, 8, 9), 6)
    3
    """
    inRange = pancakes[:flipBase]
    largest = 0
    largestOrder = -1
    for order, pancake in enumerate(inRange):
        if abs(pancake) > largest:
            largest = abs(pancake)
            largestOrder = order + 1
    return largestOrder

def sorting_step(pancakes, sortedOrder, burnt=False):
    """
    >>> sorting_step((1, 4, 6, 3, 5, 2, 7, 8, 9), 6)
    (2, 5, 3, 1, 4, 6, 7, 8, 9)
    >>> sorting_step((-1, -4, -6, 3, -5, -2, 7, 8, 9), 6, burnt=True)
    (2, 5, -3, -1, -4, 6, 7, 8, 9)
    """
    current_pos = find_largest(pancakes, sortedOrder)
    pancakes = flip_top(pancakes, current_pos, burnt)
    if pancakes[0] > 0:
        pancakes = flip_top(pancakes, 1, burnt)
    return flip_top(pancakes, sortedOrder, burnt)

def sorting_steps(pancakes, burnt=False):
    """
    >>> sorting_steps((1, 8, 5, 7, 2, 9, 4, 6, 3))
    [(1, 8, 5, 7, 2, 9, 4, 6, 3), (3, 6, 4, 1, 8, 5, 7, 2, 9), (2, 7, 5, 3, 6, 4, 1, 8, 9), (1, 4, 6, 3, 5, 2, 7, 8, 9), (2, 5, 3, 1, 4, 6, 7, 8, 9), (4, 1, 3, 2, 5, 6, 7, 8, 9), (2, 3, 1, 4, 5, 6, 7, 8, 9), (1, 2, 3, 4, 5, 6, 7, 8, 9)]
    >>> sorting_steps((1, -8, -5, 7, 2, 9, -4, -6, 3), burnt=True)
    [(1, -8, -5, 7, 2, 9, -4, -6, 3), (-3, 6, 4, 1, -8, -5, 7, 2, 9), (-2, -7, 5, -3, 6, 4, 1, 8, 9), (-1, -4, -6, 3, -5, -2, 7, 8, 9), (2, 5, -3, -1, -4, 6, 7, 8, 9), (4, 1, 3, 2, 5, 6, 7, 8, 9), (-2, -3, -1, 4, 5, 6, 7, 8, 9), (1, -2, 3, 4, 5, 6, 7, 8, 9), (1, 2, 3, 4, 5, 6, 7, 8, 9)]
    >>> sorting_steps((832, 617, 727, 478, 960, 360, 548, 925, 312, 407, 410, 706, 864, 940, 817, 452))
    [(832, 617, 727, 478, 960, 360, 548, 925, 312, 407, 410, 706, 864, 940, 817, 452), (452, 817, 940, 864, 706, 410, 407, 312, 925, 548, 360, 832, 617, 727, 478, 960), (478, 727, 617, 832, 360, 548, 925, 312, 407, 410, 706, 864, 452, 817, 940, 960), (817, 452, 864, 706, 410, 407, 312, 478, 727, 617, 832, 360, 548, 925, 940, 960), (548, 360, 832, 617, 727, 478, 312, 407, 410, 706, 817, 452, 864, 925, 940, 960), (452, 817, 706, 410, 407, 312, 478, 727, 617, 548, 360, 832, 864, 925, 940, 960), (360, 548, 617, 727, 478, 312, 407, 410, 706, 452, 817, 832, 864, 925, 940, 960), (452, 706, 410, 407, 312, 478, 360, 548, 617, 727, 817, 832, 864, 925, 940, 960), (617, 548, 360, 478, 312, 407, 410, 452, 706, 727, 817, 832, 864, 925, 940, 960), (452, 410, 407, 312, 478, 360, 548, 617, 706, 727, 817, 832, 864, 925, 940, 960), (360, 452, 410, 407, 312, 478, 548, 617, 706, 727, 817, 832, 864, 925, 940, 960), (312, 407, 410, 360, 452, 478, 548, 617, 706, 727, 817, 832, 864, 925, 940, 960), (360, 312, 407, 410, 452, 478, 548, 617, 706, 727, 817, 832, 864, 925, 940, 960), (312, 360, 407, 410, 452, 478, 548, 617, 706, 727, 817, 832, 864, 925, 940, 960)]
    """
    progressList = [pancakes,]
    for i in range(len(pancakes)):
        modified_pancakes = sorting_step(pancakes, len(pancakes)-i, burnt)
        if modified_pancakes != pancakes:
            progressList.append(modified_pancakes)
            pancakes = modified_pancakes
    return progressList
