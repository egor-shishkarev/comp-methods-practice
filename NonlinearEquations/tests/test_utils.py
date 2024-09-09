import unittest
from unittest.mock import patch
from utils import float_check, int_check


class TestFloatCheck(unittest.TestCase):
    @patch('builtins.input', return_value='3.14')
    def test_float_check_valid(self, mock_input):
        result = float_check("")
        self.assertEqual(result, 3.14)

    @patch('builtins.input', side_effect=['abc', '3.14'])
    def test_float_check_invalid_then_valid(self, mock_input):
        result = float_check("")
        self.assertEqual(result, 3.14)


class TestIntCheck(unittest.TestCase):
    @patch('builtins.input', return_value='3')
    def test_int_check_valid(self, mock_input):
        result = int_check("")
        self.assertEqual(result, 3)

    @patch('builtins.input', side_effect=['abc', '3'])
    def test_int_check_invalid_then_valid(self, mock_input):
        result = int_check("")
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
