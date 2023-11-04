
import functions
import classes

def a_star(start, target, blocked, cols, rows):

    # g = distance from start to a cell
    # h = estimated distance from cell to target
    # f = g + h
    # q = lowest f in open_list

    open_list = []
    closed_list = []

    arena = [[classes.cell() for _ in range(cols)] for _ in range(rows)]
    arena[start[0]][start[1]].value = 2
    arena[target[0]][target[1]].value = 3

    functions.init_start(arena, start, target)

    north = [start[0], start[1] - 1]
    east = [start[0] + 1, start[1]]
    south = [start[0], start[1] + 1]
    west = [start[0] - 1, start[1]]
    nearby = [north, east, south, west]

    if target in nearby:
        return [target]

    open_list.insert(0, arena[start[0]][start[1]])

    while open_list:

        q = open_list[0]

        ret = functions.get_successors(open_list, closed_list, arena, q, start, target, blocked)

        if ret == 0:

            path = functions.get_path(open_list[0], start, target)
            return path

        open_list.pop(0)

        closed_list.append(q)

    return [-1]
