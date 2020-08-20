import unittest
from demo import *


class TestDemo(unittest.TestCase):

    def test_operate(self):
        game = Game()
        game.list = [[4, 2, 4, 2], [2, 2, 4, 0], [0, 4, 2, 4], [0, 0, 2, 2]]
        game.operate('a')
        assert game.list == [[4, 2, 4, 2], [4, 4, 0, 0], [4, 2, 4, 0], [4, 0, 0, 0]]

        game.operate('d')
        assert game.list == [[4, 2, 4, 2], [0, 0, 0, 8], [0, 4, 2, 4], [0, 0, 0, 4]]

        game.operate('w')
        assert game.list == [[4, 2, 4, 2], [0, 4, 2, 8], [0, 0, 0, 8], [0, 0, 0, 0]]

        game.operate('s')
        assert game.list == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 2, 4, 2], [4, 4, 2, 16]]
