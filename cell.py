from enum import IntEnum

from geometry import Line, Point
from window import Window

class WallSide(IntEnum):
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3

class Cell:
    def __init__(self, top_left: Point, bottom_right: Point, window: Window | None = None) -> None:
        self.has_wall: list[bool] = [True, True, True, True] # Left, right, top, bottom
        self.__tl = top_left
        self.__br = bottom_right

        self.__tr = Point(bottom_right.x, top_left.y)
        self.__bl = Point(top_left.x, bottom_right.y)

        self.__window = window

    def get_center(self):
        return Point((self.__tl.x + self.__tr.x) / 2, (self.__tl.y + self.__bl.y)/2)
    
    def draw(self):
        if not self.__window:
            return
        self.__window.draw_line(Line(self.__tl, self.__bl), "black" if self.has_wall[WallSide.LEFT] else "#d9d9d9")
        self.__window.draw_line(Line(self.__tr, self.__br), "black" if self.has_wall[WallSide.RIGHT] else "#d9d9d9")
        self.__window.draw_line(Line(self.__tl, self.__tr), "black" if self.has_wall[WallSide.TOP] else "#d9d9d9")
        self.__window.draw_line(Line(self.__bl, self.__br), "black" if self.has_wall[WallSide.BOTTOM] else "#d9d9d9")
    
    def draw_move(self, to_cell: "Cell", undo=False):
        if not self.__window:
            return
        self.__window.draw_line(Line(self.get_center(), to_cell.get_center()), "gray" if undo else "red")
