import sys
from pathlib import Path

import unittest

from maze.maze_generator.maze_gui import Maze
from maze.gui.window import Window


project_root = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(project_root))


class Test(unittest.TestCase):
    def test_maze(self):
        window = Window(1000, 1000)
        num_rows = 10
        num_cols = 5
        m1 = Maze(0, 0, num_rows, num_cols, 48, window)
        self.assertEqual(len(m1.cells), num_rows * num_cols)
        self.assertEqual(len(m1.cells[0]), num_rows)
