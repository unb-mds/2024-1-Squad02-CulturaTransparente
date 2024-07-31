import sys
import os
import unittest


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from backend.functions.format import formatar

class TestFormatModule(unittest.TestCase):

    def test_formatar(self):
        self.assertEqual(formatar(1234567.89), "1.234.567.89")
        self.assertEqual(formatar(1000.0), "1.000.00")
        self.assertEqual(formatar(0.5), "0.50")
        self.assertEqual(formatar(1234), "1.234.00")

    def test_formatar_negativos(self):
        self.assertEqual(formatar(-1234567.89), "-1.234.567.89")
        self.assertEqual(formatar(-1000.0), "-1.000.00")
        self.assertEqual(formatar(-0.5), "-0.50")
        self.assertEqual(formatar(-1234), "-1.234.00")

if __name__ == '__main__':
    unittest.main()