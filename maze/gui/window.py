from tkinter import Tk, BOTH, Canvas


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title("Maze")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed")

    def close(self) -> None:
        self.__running = False

    def draw_line(self, line, color, width=1) -> None:
        line.draw(self.__canvas, color, width)

    def draw_rectangle(self, p1, p2, fill_color) -> None:
        self.__canvas.create_rectangle(
            p1.x, p1.y, p2.x, p2.y, fill=fill_color, outline=fill_color
        )

    def __str__(self) -> str:
        return "Window: {}".format(self.__root)

    def __repr__(self) -> str:
        return self.__str__()
