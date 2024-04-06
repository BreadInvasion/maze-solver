import random
import time
from cell import Cell, WallSide
from geometry import Point
from window import Window


class Maze:
    def __init__(self, top_left: Point, num_rows: int, num_cols: int, cell_size_x: int, cell_size_y: int, win: Window | None = None, seed: int = None):
        self.__tl = top_left
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x =  cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__create_cells()
        self.__break_entrance_and_exit()
        if seed:
            random.seed(seed)
        self.__break_walls_r(0,0,[])

    def __create_cells(self):
        self.__cells: list[list[Cell]] = []
        for i in range(self.__num_cols):
            col: list[Cell] = []
            for j in range(self.__num_rows):
                top_left = Point(self.__tl.x + i * self.__cell_size_x, self.__tl.y + j * self.__cell_size_y)
                bottom_right = Point(top_left.x + self.__cell_size_x, top_left.y + self.__cell_size_y)
                col.append(Cell(top_left, bottom_right, self.__win))
                col[-1].draw()
                self.__animate()
            self.__cells.append(col)
    
    def get_columns(self) -> int:
        return len(self.__cells)
    
    def get_rows(self) -> int:
        return len(self.__cells[0])
    
    def __animate(self):
        if not self.__win:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def __break_entrance_and_exit(self):
        if len(self.__cells) == 0 or len(self.__cells[0]) == 0:
            raise Exception("Cannot break entrance and exit on empty maze")
        self.__cells[0][0].has_wall[WallSide.TOP] = False
        self.__cells[0][0].draw()
        self.__animate()
        self.__cells[-1][-1].has_wall[WallSide.BOTTOM] = False
        self.__cells[-1][-1].draw()
        self.__animate()

    def __break_walls_r(self, i: int, j: int, visited: list[tuple[int, int]]):
        visited.append((i, j))
        while True:
            possible: list[WallSide] = []
            if i > 0 and (i-1, j) not in visited:
                possible.append(WallSide.LEFT)
            if i < self.__num_cols - 1 and (i+1, j) not in visited:
                possible.append(WallSide.RIGHT)
            if j > 0 and (i, j-1) not in visited:
                possible.append(WallSide.TOP)
            if j < self.__num_rows - 1 and (i, j+1) not in visited:
                possible.append(WallSide.BOTTOM)

            if len(possible) == 0:
                return

            choice = random.choice(possible)
            self.__cells[i][j].has_wall[choice] = False
            self.__cells[i][j].draw()
            self.__animate()
            if choice == WallSide.TOP:
                self.__cells[i][j-1].has_wall[WallSide.BOTTOM] = False
                self.__cells[i][j-1].draw()
                self.__animate()
                self.__break_walls_r(i, j-1, visited)
            if choice == WallSide.BOTTOM:
                self.__cells[i][j+1].has_wall[WallSide.TOP] = False
                self.__cells[i][j+1].draw()
                self.__animate()
                self.__break_walls_r(i, j+1, visited)
            if choice == WallSide.LEFT:
                self.__cells[i-1][j].has_wall[WallSide.RIGHT] = False
                self.__cells[i-1][j].draw()
                self.__animate()
                self.__break_walls_r(i-1, j, visited)
            if choice == WallSide.RIGHT:
                self.__cells[i+1][j].has_wall[WallSide.LEFT] = False
                self.__cells[i+1][j].draw()
                self.__animate()
                self.__break_walls_r(i+1, j, visited)

    def solve(self):
        return self.__solve_r(0, 0, [])

    def __solve_r(self, i: int, j: int, visited: list[tuple[int, int]]):
        visited = visited.copy()
        self.__animate()
        visited.append((i, j))
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True
        if i > 0 and (i-1, j) not in visited and self.__cells[i][j].has_wall[WallSide.LEFT] == False:
            self.__cells[i][j].draw_move(self.__cells[i-1][j])
            if self.__solve_r(i-1, j, visited):
                return True
            self.__cells[i][j].draw_move(self.__cells[i-1][j], undo=True)
        if i < self.__num_cols - 1 and (i+1, j) not in visited and self.__cells[i][j].has_wall[WallSide.RIGHT] == False:
            self.__cells[i][j].draw_move(self.__cells[i+1][j])
            if self.__solve_r(i+1, j, visited):
                return True
            self.__cells[i][j].draw_move(self.__cells[i+1][j], undo=True)
        if j > 0 and (i, j-1) not in visited and self.__cells[i][j].has_wall[WallSide.TOP] == False:
            self.__cells[i][j].draw_move(self.__cells[i][j-1])
            if self.__solve_r(i, j-1, visited):
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j-1], undo=True)
        if j < self.__num_rows and (i, j+1) not in visited and self.__cells[i][j].has_wall[WallSide.BOTTOM] == False:
            self.__cells[i][j].draw_move(self.__cells[i][j+1])
            if self.__solve_r(i, j+1, visited):
                return True
            self.__cells[i][j].draw_move(self.__cells[i][j+1], undo=True)
        return False