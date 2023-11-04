
import random

def get_random_cords(cols, rows):

	cords = [random.randint(0, cols - 1), random.randint(0, rows - 1)]
	return (cords)

def non_blocked_cords(rows, cols, blocked):

	cords = [random.randint(0, cols - 1), random.randint(0, rows - 1)]
	while cords in blocked:
		cords = [random.randint(0, cols - 1), random.randint(0, rows - 1)]
	return cords

def print_end(arena, path):

	print()
	for r in arena:
		for c in r:
			if c.pos in path:
				c.value = 1
			print(c.value, end = " ")
		print()
	print()

def print_arena(arena):

	print()
	for r in arena:
		for c in r:
			print(c.value, end = " ")
		print()
	print()

def print_list(list):
	
	for cell in list:
		print(cell.pos)
	print()

def get_f(g, h):

	return g + h

def get_q(list):

	lowest_q = list[0]
	for cell in list:
		if cell.f < lowest_q.f:
			lowest_q = cell
	return cell

def get_distance(start, target):

	distance = abs(start[0] - target[0]) + abs(start[1] - target[1])
	if distance < 0:
		distance *= -1
	return distance

def init_start(arena, start, target):

	start_cell = arena[start[0]][start[1]]

	start_cell.h = get_distance(start, target)
	start_cell.g = 0
	start_cell.f = get_f(start_cell.g, start_cell.h)
	start_cell.pos = start
	start_cell.visited = True

def init_cell(arena, parent, start, target, pos, blocked):

	cell = arena[pos[0]][pos[1]]
	cell.parent = parent
	cell.pos = pos
	cell.g = get_distance(start, cell.pos)
	cell.h = get_distance(cell.pos, target)
	cell.f = get_f(cell.g, cell.h)
	if cell.pos in blocked:
		cell.blocked == True
	return cell

def get_path(cell, start, target):

	path = []
	while cell.pos != start:
		if cell.pos not in path:
			path.insert(0, cell.pos)
			cell = cell.parent
	path.append(target)
	return path

def is_valid_cell(blocked, arena, cell):

	cols = len(arena[0])
	rows = len(arena)

	if cell[0] < rows and cell[0] >= 0 and cell[1] < cols and cell[1] >= 0 and cell not in blocked:
		return 1
	else:
		return -1

def check_f_in_list(open_list, closed_list, cell):

	for open_cell in open_list:
		if cell.pos == open_cell.pos and cell.f > open_cell.f:
			return -1
	if not closed_list:
		cell.visited = True
		open_list.append(cell)
		return 1
	else:
		for closed_cell in closed_list:
			if cell.pos == closed_cell.pos and cell.f > closed_cell.f:
				return -1
			elif cell.visited == False:
				cell.visited = True
				open_list.append(cell)
				return 1
	return -1

def get_successor(open_list, closed_list, arena, cell, start, target, blocked, direction):

	if is_valid_cell(blocked, arena, direction) == 1:
		if direction == target:
			return 0
		if arena[direction[0]][direction[1]].visited == False:
			new_cell = init_cell(arena, cell, start, target, direction, blocked)
			ret = check_f_in_list(open_list, closed_list, new_cell)
			return ret
	return -1

def get_successors(open_list, closed_list, arena, cell, start, target, blocked):

	north = [cell.pos[0], cell.pos[1] - 1]
	east = [cell.pos[0] + 1, cell.pos[1]]
	south = [cell.pos[0], cell.pos[1] + 1]
	west = [cell.pos[0] - 1, cell.pos[1]]
	directions = [north, east, south, west]

	if target in directions:
		return 0
	for direction in directions:
		ret = get_successor(open_list, closed_list, arena, cell, start, target, blocked, direction)
	return ret

def spawn_blocks(window_data, start, target, free):

	blocked = []
	for i in range(window_data.cols):
		for j in range(window_data.rows):
			y = random.randint(1, 7)
			if y % 3 == 0:
				cords = [j, i]
				if cords != start and cords != target:
					blocked.append(cords)
			else:
				cords = [j, i]
				free.append(cords)
	return blocked
