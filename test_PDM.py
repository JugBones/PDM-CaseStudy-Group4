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
        self.assertEqual(mock_stdout.getvalue(), "Total Salary: 6.110.000\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["20", "2"])
    def test_calculate_salary_2(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "Total Salary: 6.220.000\n")
    
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["15", "3"])
    def test_calculate_salary_3(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "Total Salary: 5.697.500\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["15", "1"])
    def test_calculate_salary_4(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "Total Salary: 5.532.500\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["3", "2"])
    def test_calculate_salary_5(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "Total Salary: 4.163.000\n")
    
    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["1", "1"])
    def test_calculate_salary_6(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "Total Salary: 3.915.500\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["1", "2"])
    def test_calculate_salary_7(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "Total Salary: 3.921.000\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["1", "3"])
    def test_calculate_salary_8(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "Total Salary: 3.926.500\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["-1", "27", "-1", "3"])
    def test_calculate_salary_9(self, input, mock_stdout):
        PDM.calculate_salary()
        self.longMessage = True
        self.assertEqual(mock_stdout.getvalue(), "Should be a positive Integer\nShould be a positive Integer\nTotal Salary: 6.330.000\n")

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("builtins.input", side_effect=["-1", "27", "4"])
    def test_calculate_salary_10(self, input, mock_stdout):
        with self.assertRaises(Exception):
            PDM.calculate_salary()


if __name__ == '__main__':
    main()
