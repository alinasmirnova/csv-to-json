import unittest

from src.io.csv_reader import read_csv
from src.io.exceptions import WrongFileFormatError
from tests.helpers.test_data_path import get_test_data_path


class CsvReaderTestCase(unittest.TestCase):
    def test__read_csv__file_not_exist__raise(self):
        with self.assertRaises(FileNotFoundError):
            read_csv(get_test_data_path('tests.io_tests', 'unknown.csv'))

    def test__read_csv__empty_string__raise(self):
        with self.assertRaises(ValueError):
            read_csv('')

    def test__read_csv__wrong_file_format__raise(self):
        with self.assertRaises(WrongFileFormatError):
            read_csv(get_test_data_path('tests.io_tests', 'wrong_file_format.txt'))

    def test__read_csv__file_is_empty__empty_array(self):
        file_name = get_test_data_path('tests.io_tests', 'empty.csv')
        self.assertEqual([], read_csv(file_name))

    def test__read_csv__file_with_headers__empty_array(self):
        file_name = get_test_data_path('tests.io_tests', 'headers_only.csv')
        self.assertEqual([], read_csv(file_name))

    def test__read_csv__file_with_more_column_in_row__ignore_extra_columns(self):
        expected = [{'first': '01', 'second': '02', 'third': '03'},
                    {'first': '11', 'second': '12', 'third': '13'}]
        file_name = get_test_data_path('tests.io_tests', 'more_column_in_row.csv')
        self.assertEqual(expected, read_csv(file_name))

    def test__read_csv__file_with_less_column_in_row__insert_empty_string(self):
        expected = [{'first': '01', 'second': '', 'third': ''},
                    {'first': '11', 'second': '12', 'third': '13'}]
        file_name = get_test_data_path('tests.io_tests', 'less_column_in_row.csv')
        self.assertEqual(expected, read_csv(file_name))

    def test__read_csv__correct_file__dictionary_with_values(self):
        expected = [{'first': '01', 'second': '02', 'third': '03'},
                    {'first': '11', 'second': '12', 'third': '13'},
                    {'first': '21', 'second': '22', 'third': '23'}]
        file_name = get_test_data_path('tests.io_tests', 'correct.csv')
        self.assertEqual(expected, read_csv(file_name))


if __name__ == '__main__':
    unittest.main()
