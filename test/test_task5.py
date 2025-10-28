import unittest
from Task5 import PasswordGenerator

class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        """Перевіряє, що пароль має правильну довжину"""
        gen = PasswordGenerator(level="Середній", length=10)
        password = gen.generate()
        self.assertEqual(len(password), 10)

    def test_invalid_level(self):
        """Перевіряє, що при неправильному рівні піднімається ValueError"""
        with self.assertRaises(ValueError):
            PasswordGenerator(level="Невідомий").generate()

    def test_hard_password_contains_special_chars(self):
        """Перевіряє, що у складному паролі є хоча б один спецсимвол"""
        gen = PasswordGenerator(level="Складний", length=12)
        password = gen.generate()
        self.assertTrue(any(ch in "!@#$%^&*" for ch in password))

if __name__ == "__main__":
    unittest.main()
