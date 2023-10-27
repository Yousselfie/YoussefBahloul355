import avg
import unittest

class TestAvg(unittest.TestCase):
    def test_intsAndFloats(self):
        self.assertEqual(avg.mean([53.8, 79.2, 12]), 48.33)

if __name__ == '__main__':
    unittest.main()