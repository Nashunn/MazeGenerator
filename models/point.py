#! python3.

class Point:
    """
        Class defining a point, characterized by :
        - x : x coordinate
        - y : y coordinate
        - col : column of that point on the maze
        - line : line of that point on the maze
        """
    def __init__(self, x, y, col, line):
        self.x = x
        self.y = y
        self.col = col
        self.line = line
