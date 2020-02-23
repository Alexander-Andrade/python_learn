import unittest
from main import fibonacci_numbers


class TestCache(unittest.TestCase):

    def test_cache(self):
        fibonacci_numbers(5)

        cache = {(0,): 0, (1,): 1, (2,): 1, (3,): 2, (4,): 3, (5,): 5}
        self.assertEqual(fibonacci_numbers._Cache__cache, cache)


if __name__ == '__main__':
    unittest.main()
