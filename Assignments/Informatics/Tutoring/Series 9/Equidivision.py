
def groups(grid):
    result = dict()

    labels = set()
    for row in grid:
        labels.update(set(row))

    for label in list(labels):
        result[str(label)] = {}

    for row_num, row in enumerate(grid):
        for col_num, label in enumerate(row):
            update_set = set(result[str(label)])
            update_set.add((row_num, col_num,))
            result[str(label)] = update_set

    return result


def connected(positions):
    positions = list(positions)
    start_posit = positions[0]
    for posit in positions[1:]:

        if posit[0] < start_posit[0]:
            start_posit = posit
        elif posit[0] == start_posit[0] and posit[1] < start_posit[1]:
            start_posit = posit

    positions = set(positions)
    positions.remove(start_posit)

    subconnected(start_posit, positions)

    if len(list(positions)) == 0:
        return True
    else:
        return False

def subconnected(posit, positions):
    left = posit[0]+1, posit[1]
    right = posit[0]-1, posit[1]
    up = posit[0], posit[1]+1
    down = posit[0], posit[1]-1

    further_step = list()

    if left in positions:
        positions.remove(left,)
        further_step.append(left)
    if right in positions:
        positions.remove(right,)
        further_step.append(right)
    if up in positions:
        positions.remove(up,)
        further_step.append(up)
    if down in positions:
        positions.remove(down,)
        further_step.append(down)

    for step in further_step:
        subconnected(step, positions)




#grid = [[1, 1, 1], [2, 2, 3], [2, 3, 3]]
grid = [[1, 1, 1, 5, 5], [2, 1, 5, 5, 4], [2, 1, 5, 4, 4], [2, 2, 4, 4, 3], [2, 3, 3, 3, 3]]
print(groups(grid))

print(connected({(1, 2), (1, 3), (2, 2), (0, 3), (0, 4)}))
print(connected({(1, 2), (1, 4), (2, 2), (0, 3), (0, 4)}))
"""
>>> grid = [[1, 1, 1], [2, 2, 3], [2, 3, 3]]
>>> equidivision(grid)
True

>>> grid = [[1, 1, 1], [2, 2, 3], [3, 3, 2]]
>>> equidivision(grid)
False

>>> grid = [[1, 1, 1, 5, 5], [2, 1, 5, 5, 4], [2, 1, 5, 4, 4], [2, 2, 4, 4, 3], [2, 3, 3, 3, 3]]
>>> equidivision(grid)
True
"""