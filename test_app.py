import unittest
import app

class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(app.sub(3, 2), 1)
        self.assertEqual(app.add(3, 2), 5)
        self.assertEqual(app.mul(3, 2), 6)
        self.assertEqual(app.div(3, 2), 1)

if __name__ == '__main__':
    unittest.main()
