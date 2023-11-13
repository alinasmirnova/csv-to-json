import unittest

from src.io.csv_reader import read_csv
from src.io.exceptions import WrongFileFormatError


class CsvReaderTestCase(unittest.TestCase):
    def test__read_csv__file_not_exist__raise(self):
        with self.assertRaises(FileNotFoundError):
            read_csv('./test_data/unknown.csv')

    def test__read_csv__empty_string__raise(self):
        with self.assertRaises(ValueError):
            read_csv('')

    def test__read_csv__wrong_file_format__raise(self):
        with self.assertRaises(WrongFileFormatError):
            read_csv('./test_data/wrong_file_format.txt')

    def test__read_csv__file_is_empty__empty_array(self):
        self.assertEqual([], read_csv('./test_data/empty.csv'))

    def test__read_csv__file_with_headers__empty_array(self):
        self.assertEqual([], read_csv('./test_data/headers_only.csv'))

    def test__read_csv__file_with_more_column_in_row__ignore_extra_columns(self):
        expected = [{'first': '01', 'second': '02', 'third': '03'},
                    {'first': '11', 'second': '12', 'third': '13'}]
        self.assertEqual(expected, read_csv('test_data/more_column_in_row.csv'))

    def test__read_csv__file_with_less_column_in_row__insert_empty_string(self):
        expected = [{'first': '01', 'second': '', 'third': ''},
                    {'first': '11', 'second': '12', 'third': '13'}]
        self.assertEqual(expected, read_csv('test_data/less_column_in_row.csv'))

    def test__read_csv__correct_file__dictionary_with_values(self):
        expected = [{'first': '01', 'second': '02', 'third': '03'},
                    {'first': '11', 'second': '12', 'third': '13'},
                    {'first': '21', 'second': '22', 'third': '23'}]
        self.assertEqual(expected, read_csv('./test_data/correct.csv'))


if __name__ == '__main__':
    unittest.main()
