
import pygame

class create_window():
	
    def __init__(self, width, height, cols, rows, colour):
	    
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        self.block_width = width / cols
        self.block_height = height / rows
        self.colour = colour
        self.cols = cols
        self.rows = rows

class cell():

    def __init__(self):

        self.visited = False
        self.value = 0
        self.pos = []
        self.h = -1
        self.g = -1
        self.f = -1
        self.parent = []
        self.blocked = False