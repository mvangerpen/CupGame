import cup_game
import unittest
from unittest import mock
from unittest.mock import patch
from unittest.mock import MagicMock

class TestCupGame(unittest.TestCase):

    def test_getChoice(self):
        test_input = 4
        cup_game.input = MagicMock(side_effect=test_input)

        choice = cup_game.getChoice(int, 'Expecting integer: ')
        self.assertEqual(choice, test_input)


    def test_isWinner(self):
        stone = 4
        choice = 5
        self.assertTrue(cup_game.isWinner(stone, choice))

        choice = 7
        self.assertFalse(cup_game.isWinner(stone, choice))

    def test_bankWin(self):
        result = cup_game.bankWin(100, 20, 4)
        self.assertEqual(result, 180)

        result = cup_game.bankWin(300, 10, 40)
        self.assertEqual(result, 700)

    def test_bankLose(self):
        result = cup_game.bankLose(100, 20)
        self.assertEqual(result, 80)

        result = cup_game.bankLose(100, 100)
        self.assertEqual(result, 0)

    

if __name__ == '__main__':
    unittest.main()
