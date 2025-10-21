import unittest
import Task5

class TestTask5(unittest.TestCase):
    def test_exists(self):
        self.assertTrue(hasattr(Task5, "__doc__"))

if __name__ == "__main__":
    unittest.main()
  
