from maze.gui.window import Window
from maze.gui.cell import Cell
from maze.gui.point import Point
import time
import random
from pprint import pprint


class Maze:
    def __init__(
        self,
        x1: float,
        y1: float,
        num_rows: int,
        num_cols: int,
        cell_size: float,
        window: Window | None = None,
        seed: int | None = None,
    ) -> None:
        self.cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size = cell_size
        self._window = window
        if seed != None:
            self._seed = random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_wall_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self) -> None:
        if self._window == None:
            raise Exception("Window not initialized")
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._window))
            self.cells.append(col_cells)
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, col: int, row: int) -> None:
        x_start = self._x1 + col * self._cell_size
        y_start = self._y1 + row * self._cell_size
        x_end = x_start + self._cell_size
        y_end = y_start + self._cell_size
        self.cells[col][row].draw(Point(x_start, y_start), Point(x_end, y_end))
        self._animate()

    def _animate(self) -> None:
        if self._window == None:
            raise Exception("Window not initialized")
        self._window.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self) -> None:
        self.cells[0][0].walls["left"] = False
        self._draw_cell(0, 0)
        self.cells[self._num_cols - 1][self._num_rows - 1].walls["right"] = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)

    def _get_neighbors(self, col: int, row: int) -> list[tuple[int, int]]:
        neighbors = []
        if col > 0 and not self.cells[col - 1][row].visited:
            neighbors.append((col - 1, row))
        if row > 0 and not self.cells[col][row - 1].visited:
            neighbors.append((col, row - 1))
        if col < self._num_cols - 1 and not self.cells[col + 1][row].visited:
            neighbors.append((col + 1, row))
        if row < self._num_rows - 1 and not self.cells[col][row + 1].visited:
            neighbors.append((col, row + 1))
        return neighbors

    def _break_wall_r(self, col: int, row: int) -> None:
        self.cells[col][row].visited = True
        self._draw_cell(col, row)
        while True:
            neighbors = self._get_neighbors(col, row)
            if len(neighbors) == 0:
                return
            neighbor = random.choice(neighbors)

            if neighbor[0] < col:
                self.cells[col][row].walls["left"] = False
                self.cells[neighbor[0]][neighbor[1]].walls["right"] = False
            elif neighbor[0] > col:
                self.cells[col][row].walls["right"] = False
                self.cells[neighbor[0]][neighbor[1]].walls["left"] = False
            elif neighbor[1] < row:
                self.cells[col][row].walls["top"] = False
                self.cells[neighbor[0]][neighbor[1]].walls["bottom"] = False
            elif neighbor[1] > row:
                self.cells[col][row].walls["bottom"] = False
                self.cells[neighbor[0]][neighbor[1]].walls["top"] = False

            self._draw_cell(col, row)
            self._break_wall_r(neighbor[0], neighbor[1])

    def _reset_cells_visited(self) -> None:
        for col in self.cells:
            for cell in col:
                cell.visited = False

    def solve(self) -> None:
        self._solve_r(0, 0, self._num_cols - 1, self._num_rows - 1)

    def _solve_r(self, col: int, row: int, end_col: int, end_row: int) -> bool:
        self._animate()
        self.cells[col][row].visited = True
        if col == end_col and row == end_row:
            return True
        neighbors = self._get_neighbors(col, row)
        for n in neighbors:
            direction = ""
            if col > n[0]:
                direction = "left"
            elif col < n[0]:
                direction = "right"
            elif row > n[1]:
                direction = "top"
            elif row < n[1]:
                direction = "bottom"

            if (
                direction
                and not self.cells[col][row].walls[direction]
                and not self.cells[n[0]][n[1]].visited
            ):
                result = self._solve_r(n[0], n[1], end_col, end_row)
                if result:
                    self.cells[col][row].draw_move(self.cells[n[0]][n[1]])
                    return True
                else:
                    self.cells[col][row].draw_move(self.cells[n[0]][n[1]], undo=True)
        return False
