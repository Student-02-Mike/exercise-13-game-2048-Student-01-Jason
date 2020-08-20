import unittest
from demo import *


class TestDemo(unittest.TestCase):

    def test_operate(self):
        game = Game()
        game.list = [[4, 2, 4, 2], [2, 2, 4, 0], [0, 4, 2, 4], [0, 0, 2, 2]]

        # TODO
