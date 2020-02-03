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
        self.assertIsInstance(result, ValueError)
    
    def test_do_staff3(self):
        test_param = None
        result = main.do_staff(test_param)
        # https://docs.python.org/3/library/unittest.html
        self.assertEqual(result, 'plese enter a number')

    def test_do_staff4(self):
        test_param = ''
        result = main.do_staff(test_param)
        self.assertEqual(result, 'plese enter a number')
    
    def test_do_staff5(self):
        test_param = 0
        result = main.do_staff(test_param)
        # https://docs.python.org/3/library/unittest.html
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
