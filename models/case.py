#! python3.
import pygame
from MazeGenerator.models.point import Point

pygame.font.init()
font = pygame.font.SysFont(None, 20)

COLOR_LINE = (10, 10, 10)

class Case:
    """
    Class that define a case of the maze, defined by :
    - id : Id of the case in the maze
    - coord : Coordinate of the corner top left of the case
    - sizeCase : Size of the cases in the maze
    - walls : list of walls (T for top, B for Bottom, L for left, R for right)
    """

    def __init__(self, id: int, coord: Point, sizeCase: int):
        self.id = id
        self.coord = coord
        self.sizeCase = sizeCase
        self.walls = []

    def get_coord_tl(self):
        """ Get coord top left of the case """
        return self.coord

    def get_coord_tr(self):
        """ Get coord top right of the case """
        return Point((self.coord.x + self.sizeCase), self.coord.y, -1, -1)

    def get_coord_bl(self):
        """ Get coord bottom left of the case """
        return Point(self.coord.x, (self.coord.y + self.sizeCase), -1, -1)

    def get_coord_br(self):
        """ Get coord bottom right of the case """
        return Point((self.coord.x + self.sizeCase), (self.coord.y + self.sizeCase), -1, -1)

    def add_wall_top(self):
        """ Add a wall at the top of the case """
        self.walls.append('T')

    def add_wall_bottom(self):
        """ Add a wall at the bottom of the case """
        self.walls.append('B')

    def add_wall_left(self):
        """ Add a wall at the left of the case """
        self.walls.append('L')

    def add_wall_right(self):
        """ Add a wall at the right of the case """
        self.walls.append('R')

    def draw_wall_top(self, screen):
        """ Draw a wall at the top of the case """
        p_start = self.get_coord_tl()
        p_end = self.get_coord_tr()
        pygame.draw.line(screen, COLOR_LINE, (p_start.x, p_start.y), (p_end.x, p_end.y))

    def draw_wall_bottom(self, screen):
        """ Draw a wall at the bottom of the case """
        p_start = self.get_coord_bl()
        p_end = self.get_coord_br()
        pygame.draw.line(screen, COLOR_LINE, (p_start.x, p_start.y), (p_end.x, p_end.y))

    def draw_wall_left(self, screen):
        """ Draw a wall at the left of the case """
        p_start = self.get_coord_tl()
        p_end = self.get_coord_bl()
        pygame.draw.line(screen, COLOR_LINE, (p_start.x, p_start.y), (p_end.x, p_end.y))

    def draw_wall_right(self, screen):
        """ Draw a wall at the right of the case """
        p_start = self.get_coord_tr()
        p_end = self.get_coord_br()
        pygame.draw.line(screen, COLOR_LINE, (p_start.x, p_start.y), (p_end.x, p_end.y))

    def print(self):
        """ Print case info in console """
        print(
            "Case " + str(self.id) + " : [" + str(self.coord.col) + "," + str(self.coord.line) + "] (" +
            str(self.coord.x) + "," + str(self.coord.y) + ")\n"
        )

    def draw_id(self, screen):
        text = font.render(str(self.id), False, COLOR_LINE)
        screen.blit(text, (self.coord.x + (self.sizeCase/2), self.coord.y + (self.sizeCase/2)))

    def draw_walls(self, screen):
        """ Draw walls with pygame """
        # print('WALLS of cell ' + str(self.id) + ' : ' + str(self.walls))
        # self.print()
        if 'R' in self.walls:
            # If there is a right wall, draw it
            self.draw_wall_right(screen)
        if 'L' in self.walls:
            # If there is a left wall, draw it
            self.draw_wall_left(screen)
        if 'T' in self.walls:
            # If there is a top wall, draw it
            self.draw_wall_top(screen)
        if 'B' in self.walls:
            # If there is a bottom wall, draw it
            self.draw_wall_bottom(screen)