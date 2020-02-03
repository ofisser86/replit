import unittest
import main

class TestMain(unittest.TestCase):
    def test_do_staff(self):
        test_param = 10
        result = main.do_staff(test_param)
        self.assertEqual(result, 15)
    
    def test_do_staff2(self):
        test_param = 'gdfsgsdfg'
        result = main.do_staff(test_param)
        # https://docs.python.org/3/library/unittest.html
        self.assertTrue(isinstance(result, ValueError))


unittest.main()
