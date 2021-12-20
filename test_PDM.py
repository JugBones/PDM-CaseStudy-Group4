import io
import PDM
from unittest import main
from unittest.mock import patch
from unittest import TestCase

test_params = []

class Test(TestCase):

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["20", "1"])
    def test_calculate_salary_1(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "________________________\nOvertime Pay: 2.200.000\nBasic Salary: 3.800.000\nAllowance: 190.000\n________________________\nTotal Salary: 6.190.000\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["20", "2"])
    def test_calculate_salary_2(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "________________________\nOvertime Pay: 2.200.000\nBasic Salary: 3.800.000\nAllowance: 380.000\n________________________\nTotal Salary: 6.380.000\n")
    
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["15", "3"])
    def test_calculate_salary_3(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "________________________\nOvertime Pay: 1.650.000\nBasic Salary: 3.800.000\nAllowance: 570.000\n________________________\nTotal Salary: 6.020.000\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["15", "1"])
    def test_calculate_salary_4(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "________________________\nOvertime Pay: 1.650.000\nBasic Salary: 3.800.000\nAllowance: 190.000\n________________________\nTotal Salary: 5.640.000\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["3", "2"])
    def test_calculate_salary_5(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "________________________\nOvertime Pay: 330.000\nBasic Salary: 3.800.000\nAllowance: 380.000\n________________________\nTotal Salary: 4.510.000\n")
    
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["1", "1"])
    def test_calculate_salary_6(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "________________________\nOvertime Pay: 110.000\nBasic Salary: 3.800.000\nAllowance: 190.000\n________________________\nTotal Salary: 4.100.000\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["1", "2"])
    def test_calculate_salary_7(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "________________________\nOvertime Pay: 110.000\nBasic Salary: 3.800.000\nAllowance: 380.000\n________________________\nTotal Salary: 4.290.000\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["1", "3"])
    def test_calculate_salary_8(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "________________________\nOvertime Pay: 110.000\nBasic Salary: 3.800.000\nAllowance: 570.000\n________________________\nTotal Salary: 4.480.000\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["-1", "27", "19", "-1", "3"])
    def test_calculate_salary_9(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "Should be a positive integer below 21\nShould be a positive integer below 21\nShould be an integer between 0 and 4\n________________________\nOvertime Pay: 2.090.000\nBasic Salary: 3.800.000\nAllowance: 570.000\n________________________\nTotal Salary: 6.460.000\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["-1", "27", "19","4"])
    def test_calculate_salary_10(self, input, mock_stdout):
        with self.assertRaises(Exception):
            PDM.calculate_salary()


if __name__ == '__main__':
    main()
