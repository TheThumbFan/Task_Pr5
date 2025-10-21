import unittest
from Task5 import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        gen = PasswordGenerator(level="Середній", length=10)
        password = gen.generate()
        self.assertEqual(len(password), 10)

    def test_invalid_level(self):
        with self.assertRaises(ValueError):
            PasswordGenerator(level="Невідомий").generate()

if __name__ == "__main__":
    unittest.main()
