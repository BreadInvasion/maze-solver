from cell import Cell
from geometry import Line, Point
from window import Window

def main():
    window = Window(800, 600)

    for i in range(5):
        for j in range(5):
            cell = Cell(Point(100 * i + 50, 100 * j + 50), Point(100 * i + 150, 100 * j + 150), window)
            cell.draw()

    window.wait_for_close()

if __name__ == "__main__":
    main()