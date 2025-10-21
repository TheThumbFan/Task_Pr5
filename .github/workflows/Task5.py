import random
import string

class PasswordGenerator:
    def __init__(self, level="Середній", length=12):
        self.level = level
        self.length = max(6, min(length, 20))  # обмеження 6–20 символів

    def generate(self):
        if self.level == "Легкий":
            chars = string.ascii_lowercase + string.digits
        elif self.level == "Середній":
            chars = string.ascii_letters + string.digits
        elif self.level == "Складний":
            chars = string.ascii_letters + string.digits + "!@#$%^&*"
        else:
            raise ValueError("Рівень має бути: Легкий, Середній або Складний"

        return ''.join(random.choice(chars) for _ in range(self.length))
                             
# Демонстрація
if __name__ == "__main__":
    gen = PasswordGenerator(level="Середній", length=12)
    password = gen.generate()
    print("Згенерований пароль:", password)
