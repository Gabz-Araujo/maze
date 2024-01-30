from tkinter import BOTH, Canvas

from maze.gui.point import Point


class Line:
    def __init__(self, start: Point, end: Point) -> None:
        self.start = start
        self.end = end

    def draw(self, canvas: Canvas, fill_color: str, line_width: int = 1) -> None:
        canvas.create_line(
            self.start.x,
            self.start.y,
            self.end.x,
            self.end.y,
            fill=fill_color,
            width=line_width,
        )
        canvas.pack(fill=BOTH, expand=1)

    def __str__(self) -> str:
        return "Start: {}, End: {}".format(self.start, self.end)

    def __repr__(self) -> str:
        return self.__str__()
