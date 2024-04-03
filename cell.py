from enum import IntEnum

from geometry import Line, Point
from window import Window

class WallSide(IntEnum):
    LEFT = 0
    RIGHT = 1
    TOP = 2
    BOTTOM = 3

class Cell:
    def __init__(self, top_left: Point, bottom_right: Point, window: Window) -> None:
        self.has_wall: list[bool] = [True, True, True, True] # Left, right, top, bottom
        self.__tl = top_left
        self.__br = bottom_right

        self.__tr = Point(bottom_right.x, top_left.y)
        self.__bl = Point(top_left.x, bottom_right.y)

        self.__window = window
    
    def draw(self):
        if self.has_wall[WallSide.LEFT]:
            self.__window.draw_line(Line(self.__tl, self.__bl), "black")
        if self.has_wall[WallSide.RIGHT]:
            self.__window.draw_line(Line(self.__tr, self.__br), "black")
        if self.has_wall[WallSide.TOP]:
            self.__window.draw_line(Line(self.__tl, self.__tr), "black")
        if self.has_wall[WallSide.RIGHT]:
            self.__window.draw_line(Line(self.__bl, self.__br), "black")
