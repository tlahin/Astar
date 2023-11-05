
import pygame

import functions
import Astar
import classes

pygame.init()

pygame.display.set_caption("Astar demo by tlahin")

cols, rows = (80, 80)
random_pos = True

window_data = classes.create_window(800, 900, cols, rows, 'black')

if random_pos:

    start_pos = functions.get_random_cords(cols, rows)
    target_pos = functions.get_random_cords(cols, rows)

    while target_pos == start_pos:

        target_pos = functions.get_random_cords(cols, rows)

path = []
free = []
blocked = functions.spawn_blocks(window_data, start_pos, target_pos, free)

flag = False
running = True
start = True

path = Astar.a_star(start_pos, target_pos, blocked, cols, rows)
while path == [-1]:
    start_pos = functions.non_blocked_cords(cols, rows, blocked)
    target_pos = functions.non_blocked_cords(cols, rows, blocked)
    path = Astar.a_star(start_pos, target_pos, blocked, cols, rows)

while running:

    pygame.display.flip()

    window_data.window.fill('black', pygame.Rect(0, 0, window_data.width, window_data.height))
    pygame.draw.rect(window_data.window, ('gray'), pygame.Rect(0, window_data.height - 100, window_data.width, 100))

    # Get inputs
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            new_pos = [round(event.pos[0] / window_data.block_width), round(event.pos[1] / window_data.block_height)]
            if new_pos[0] < rows and new_pos[0] >= 0 and new_pos[1] < cols and new_pos[1] >= 0 and new_pos not in blocked:
                start_pos = new_pos
            path = Astar.a_star(start_pos, target_pos, blocked, cols, rows)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_t:

                flag = not flag

                if flag == True:
                    window_data.colour = 'green'
                else:
                    window_data.colour = 'black'

    if path == [-1]:
        print("No path available")
        running = False

    else:

        # Renders the path from start to target (path is a list of cordinates)
        for node in path:
            pygame.draw.rect(window_data.window, window_data.colour, pygame.Rect(node[0] * window_data.block_width, node[1] * window_data.block_height, window_data.block_width, window_data.block_height))

        # Renders the start node
        pygame.draw.rect(window_data.window, 'white', pygame.Rect(start_pos[0] * window_data.block_width, start_pos[1] * window_data.block_height, window_data.block_width, window_data.block_height))

        # Renders the target node
        pygame.draw.rect(window_data.window, 'white', pygame.Rect(target_pos[0] * window_data.block_width, target_pos[1] * window_data.block_height, window_data.block_width, window_data.block_height))

        # Renders blocked cells
        for cell in blocked:
            pygame.draw.rect(window_data.window, 'red', pygame.Rect(cell[0] * window_data.block_width, cell[1] * window_data.block_height, window_data.block_width, window_data.block_height))
        
        functions.score_board(window_data, path)