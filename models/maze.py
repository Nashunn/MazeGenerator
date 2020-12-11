#! python3.
import pygame
import random as rand
from MazeGenerator.models.case import Case
from MazeGenerator.models.point import Point


class Maze:
    """
    Class defining a maze base, characterized by :
    - width : Width of the maze (default : 50)
    - height : Height of the maze (default : 50)
    - sizeCase : Size of the side of a case in the maze (default : 10)
    """

    def __init__(self, width=25, height=25, sizeCase=20):
        pygame.init()  # Init pygame
        self.width = width
        self.height = height
        self.sizeCase = sizeCase
        self.screen = pygame.display.set_mode((width * sizeCase, height * sizeCase))  # Screen for the maze
        pygame.display.set_caption('Maze generator')  # Set screen name
        self.screen.fill((240, 240, 240))
        self.clock = pygame.time.Clock()  # Clock to check update speed
        self.fps = 60  # This variable will define how many frames we update per second.
        self.grid = []  # Grid of cases for the maze
        self.fill_grid()
        self.start: Case = self.grid[0]  # Start of the maze
        self.end: Case = self.grid[len(self.grid) - 1]  # End of the maze
        self.generate_start_end()
        self.generate_base_walls()

    def run(self):
        # Display loop
        while True:
            self.clock.tick(self.fps)

            # Check if user is quitting
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            pygame.display.update()

    def fill_grid(self):
        """ Fill the grid with Case """
        idCase = 0
        for line in range(self.height):
            for col in range(self.width):
                case = Case(
                    idCase,
                    Point(col * self.sizeCase, line * self.sizeCase, col, line),
                    self.sizeCase
                )
                self.grid.append(case)  # Add Case into the maze grid
                idCase += 1  # Increment the id of the case

    def generate_start_end(self):
        """ Identify a start and an end case for the maze """
        startId = rand.randint(0, len(self.grid) - 1)  # Find an id randomly in the maze grid
        spaceUnit = int((len(self.grid)) / 4)  # Space unit to space the end from the start (unit = 1/4 of maze)
        endId = rand.randint((startId + 2*spaceUnit), (startId + 3*spaceUnit)) % (len(self.grid) - 1)  # Place end between : (start + 2/4) or (start + 3/4) modulo maxCase
        # Set Start and End
        self.start: Case = self.grid[startId]
        self.end: Case = self.grid[endId]
        # Identify them with color on the maze
        self.start.set_bg(self.screen, (100, 180, 100))
        self.end.set_bg(self.screen, (180, 100, 100))

    def generate_base_walls(self):
        """ Generate base walls all around the maze """
        lastLine = self.height  # Info first line is 0
        lastCol = self.width  # Info first col is 0
        # Set walls on top of first line and on bottom of last line
        for col in range(lastCol):
            caseFirstLine: Case = self.find_case_by_coord(col, 0)
            caseLastLine: Case = self.find_case_by_coord(col, lastLine - 1)
            caseFirstLine.add_wall_top()
            caseLastLine.add_wall_bottom()
        for line in range(lastLine):
            caseFirstCol: Case = self.find_case_by_coord(0, line)
            caseLastCol: Case = self.find_case_by_coord(lastCol - 1, line)
            caseFirstCol.add_wall_left()
            caseLastCol.add_wall_right()

    def print_grid(self):
        """ Print the grid with case number in console """
        idCase = 0
        result = ""
        for col in range(self.height):
            for line in range(self.width):
                case = self.grid[idCase]  # Get Case
                result += '0' + str(case.id) + " " if case.id < 10 else str(case.id) + " "  # Add to the result
                idCase += 1
            result += "\n"
        print(result)

    def draw_grid(self):
        """ Draw the grid with pygame """
        lastCase: Case = self.find_case_by_coord(self.width - 1, self.height - 1)
        for idCase in range(lastCase.id + 1):
            case = self.grid[idCase]  # Get case
            case.draw_walls(self.screen)

    def find_case_by_coord(self, col, line):
        """ Find the id of a case in the maze by col and line numbers """
        return self.grid[(line * self.width) + col]
