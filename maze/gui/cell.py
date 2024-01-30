from maze.gui.line import Line
from maze.gui.window import Window
from maze.gui.point import Point


class Cell:
    def __init__(self, win: Window) -> None:
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}
        self._p1 = None
        self._p2 = None
        self.win = win
        self.visited = False
        self.center = self.get_center()

    def get_center(self) -> Point | None:
        if self._p1 and self._p2:
            return Point((self._p1.x + self._p2.x) / 2, (self._p1.y + self._p2.y) / 2)

    def draw(self, _p1: Point, _p2: Point) -> None:
        self._p1 = _p1
        self._p2 = _p2
        self.center = self.get_center()

        # if self.visited:
        #     self.win.draw_rectangle(
        #         _p1, _p2, fill_color="grey"
        #     )  # Change to the desired background colorcell

        wall_coords = {
            "top": [Point(_p1.x, _p1.y), Point(_p2.x, _p1.y)],
            "right": [Point(_p2.x, _p1.y), Point(_p2.x, _p2.y)],
            "bottom": [Point(_p2.x, _p2.y), Point(_p1.x, _p2.y)],
            "left": [Point(_p1.x, _p2.y), Point(_p1.x, _p1.y)],
        }
        for wall, state in self.walls.items():
            color = "black" if state else "white"  # set color based on state
            self.win.draw_line(Line(*wall_coords[wall]), color=color)

    def draw_move(self, to_cell, undo: bool = False) -> None:
        color = "red" if undo else "gray"
        width = 1 if undo else 3
        if self.center and to_cell.center:
            self.win.draw_line(
                Line(self.center, to_cell.center), color=color, width=width
            )

    def __str__(self) -> str:
        return """
        Cell:
            Walls: {}
            Visited: {}
            Center: {}
        """.format(
            self.walls, self.visited, self.center
        )

    def __repr__(self) -> str:
        return self.__str__()
