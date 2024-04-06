import unittest

from geometry import Point
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        maze = Maze(top_left=Point(0,0), num_rows=10, num_cols=12, cell_size_x=10, cell_size_y=10)
        self.assertEqual(maze.get_columns(), 12)
        self.assertEqual(maze.get_rows(), 10)

if __name__ == "__main__":
    unittest.main()