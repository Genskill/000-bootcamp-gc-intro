import unittest

from largest import largest

class TestLargest(unittest.TestCase):
    def test_first(self):
        self.assertEqual(largest(3,2,1),3)

    def test_second(self):
        self.assertEqual(largest(2,3,1),3)

    def test_third(self):
        self.assertEqual(largest(2,1,3),3)

if __name__ == '__main__':
    unittest.main()
