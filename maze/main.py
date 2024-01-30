from .gui.window import Window
from .maze_generator.maze_gui import Maze
import random


def main():
    seed = random.randint(0, 100000)
    window = Window(1000, 1000)
    maze = Maze(50, 50, 10, 10, 50, window, seed)
    maze.solve()
    window.wait_for_close()


if __name__ == "__main__":
    main()
