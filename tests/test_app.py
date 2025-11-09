import unittest

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(
            greet("World"),
            "Hello, World fromFirstName LastName!"
        )


if __name__ == "__main__":
    unittest.main()