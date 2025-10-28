import random
import string

class PasswordGenerator:
    """
    Клас для реалізації генерації паролів різного рівня складності.
    Рівні: Легкий, Середній, Складний.
    Довжина паролю обмежена від 6 до 20 символів.
    """

    def __init__(self, level: str = "Середній", length: int = 12):
        """
        Ініціалізація генератора паролів.

        :param level: Рівень складності ("Легкий", "Середній", "Складний")
        :param length: Бажана довжина паролю (мін. 6, макс. 20)
        """
        self.level = level
        self.length = max(6, min(length, 20))  # обмеження 6–20 символів

    def get_charset(self) -> str:
        """
        Повертає набір символів відповідно до рівня складності.
        :return: рядок із допустимими символами
        """
        if self.level == "Легкий":
            return string.ascii_lowercase + string.digits
        elif self.level == "Середній":
            return string.ascii_letters + string.digits
        elif self.level == "Складний":
            return string.ascii_letters + string.digits + "!@#$%^&*"
        else:
            raise ValueError("Рівень має бути: Легкий, Середній або Складний")

    def generate(self) -> str:
        """
        Генерує пароль заданої довжини.
        :return: згенерований пароль
        """
        charset = self.get_charset()
        return ''.join(random.choice(charset) for _ in range(self.length))


# Демонстрація
if __name__ == "__main__":
    gen = PasswordGenerator(level="Середній", length=12)
    password = gen.generate()
    print("Згенерований пароль:", password)
    
