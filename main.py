from cell import Cell
from geometry import Line, Point
from maze import Maze
from window import Window

def main():
    window = Window(800, 600)

    maze = Maze(Point(20,20), 10, 10, 50, 50, window)
    maze.solve()
    window.wait_for_close()

if __name__ == "__main__":
    main()