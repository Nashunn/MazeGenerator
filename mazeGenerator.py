#! python3.
from MazeGenerator.models.maze import Maze
from MazeGenerator.algorithms.recursiveDivision import generate_maze

# Main
maze = Maze()
generate_maze(maze)
