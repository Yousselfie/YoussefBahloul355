import avg
import unittest

class TestAvg(unittest.TestCase):
    def test_chars(self):
        with self.assertRaises(TypeError):
            avg.mean(['a', 11.5, 'b', 23, 19.60])

if __name__ == "__main__":
    unittest.main()