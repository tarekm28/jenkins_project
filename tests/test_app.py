import unittest
from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet("World"),
            "Hello, I'm Tarek Mourad!"
        )


if __name__ == "__main__":
    unittest.main()