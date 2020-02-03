import unittest
import exerc193test as game

class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = game.run_guess(guess, answer)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = game.run_guess(1, 3)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = game.run_guess(5, 11)
        self.assertFalse(result)
    
    def test_input_wrong_type(self):
        result = game.run_guess(5, 11)
        self.assertFalse(result)    


if __name__ == '__main__':
    unittest.main()
