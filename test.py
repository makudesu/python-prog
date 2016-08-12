import unittest
from noelse import with_else, without_else


class WithElseTestCase(unittest.TestCase):

    def test_with_else_is_true(self):
        self.assertTrue(with_else(True))

    def test_with_else_is_false(self):
        self.assertFalse(with_else(False))


class WithoutElseTestCase(unittest.TestCase):

    def test_without_else_is_true(self):
        self.assertTrue(without_else(True))

    def test_without_else_is_false(self):
        self.assertFalse(without_else(False))

if __name__ == '__main__':
    unittest.main()
