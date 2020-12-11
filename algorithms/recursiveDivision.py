#! python3.
import random as rand
import pygame

from MazeGenerator.models.case import Case
from MazeGenerator.models.maze import Maze

HORIZONTAL = 'HORIZONTAL'
VERTICAL = 'VERTICAL'

def generate_maze(maze: Maze):
    """ Generate a maze following the recursive division algorithm"""
    # maze.print_grid()
    # Generate walls in maze
    generate_walls(maze)
    # Update display
    maze.draw_grid()
    # Display loop
    while True:
        maze.clock.tick(maze.fps)
        # Check if user is quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        pygame.display.update()

def generate_walls(maze: Maze):
    """ General method to initiate the creation of walls """
    start: Case = maze.find_case_by_coord(0, 0)
    end: Case = maze.find_case_by_coord(maze.width - 1, maze.height - 1)
    divide(maze, start, end)

def divide(maze: Maze, start: Case, end: Case):
    """ Divide recursively by taking a start case and an end case """
    width = abs(start.coord.col - end.coord.col)
    height = abs(start.coord.line - end.coord.line)
    # If possible to divide again, do it
    if width >= 1 or height >= 1:
        # Choose orientation
        orientation = choose_orientation(width, height)
        if orientation == VERTICAL:
            divide_vertical(maze, start, end)
        else:
            divide_horizontal(maze, start, end)

def choose_orientation(width, height):
    """ Choose orientation depending of the width and height """
    if width < height:
        result = HORIZONTAL
    elif height < width:
        result = VERTICAL
    # If height and width are equal, choose randomly
    else:
        randInt = rand.randrange(2)
        if randInt == 0:
            result = VERTICAL
        else:
            result = HORIZONTAL
    return result

def divide_vertical(maze: Maze, start: Case, end: Case):
    """ Divide maze vertically """
    chosenCol: int = rand.randint(start.coord.col, (end.coord.col - 1))  # From start to end-1 to avoid writing on an existing limit
    case1: Case = maze.find_case_by_coord(chosenCol, end.coord.line)  # Get case to end first division
    case2: Case = maze.find_case_by_coord((chosenCol + 1), start.coord.line)  # Get case to start second division
    # create walls vertically
    generate_wall(maze, case2, maze.find_case_by_coord(chosenCol + 1, end.coord.line), VERTICAL)
    # Call recursively divide
    divide(maze, start, case1)
    divide(maze, case2, end)

def divide_horizontal(maze: Maze, start: Case, end: Case):
    """ Divide maze horizontally """
    chosenLine: int = rand.randint(start.coord.line, (end.coord.line - 1))  # From start to end-1 to avoid writing on an existing limit
    case1: Case = maze.find_case_by_coord(end.coord.col, chosenLine)  # Get case to end first division
    case2: Case = maze.find_case_by_coord(start.coord.col, (chosenLine + 1))  # Get case to start second division
    # create walls horizontally
    generate_wall(maze, case2, maze.find_case_by_coord(end.coord.col, chosenLine + 1), HORIZONTAL)
    # Call recursively divide
    divide(maze, start, case1)
    divide(maze, case2, end)

def generate_wall(maze: Maze, start: Case, end: Case, orientation):
    """ Add a wall from start to end following orientation """
    if orientation == VERTICAL:
        # Get Case line by line
        holeInWall: int = rand.randint(start.coord.line, end.coord.line)
        for line in range(start.coord.line, end.coord.line + 1):
            if line != holeInWall:
                selectedCase: Case = maze.find_case_by_coord(start.coord.col, line)
                selectedCase.add_wall_left()
    elif orientation == HORIZONTAL:
        # Get Case col by col
        holeInWall: int = rand.randint(start.coord.col, end.coord.col)
        for col in range(start.coord.col, end.coord.col + 1):
            if col != holeInWall:
                selectedCase: Case = maze.find_case_by_coord(col, start.coord.line)
                selectedCase.add_wall_top()
