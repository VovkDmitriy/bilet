import unittest
import mainApp as app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.app = app
    
    def test_calculate(self):
        self.assertEqual(app.calculate(5), 13)

if __name__ == '__main__':
    unittest.main()