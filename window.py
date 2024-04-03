from tkinter import Tk, BOTH, Canvas

from geometry import Line

class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title = "Maze Generator"
        self.__canvas = Canvas(width=width, height=height)
        self.__canvas.pack()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()
    
    def draw_line(self, line: Line, fill_color: str):
        line.draw(self.__canvas, fill_color)

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self) -> None:
        self.__running = False