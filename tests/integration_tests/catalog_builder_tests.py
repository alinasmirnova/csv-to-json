import json
import unittest

from src.fc.catalog.catalog_builder import CatalogBuilder


class CatalogBuilderTestCase(unittest.TestCase):
    def test__build_catalog_empty_list_raise(self):
        with self.assertRaises(ValueError):
            CatalogBuilder._build_catalog([])

    def test__build_catalog(self):
        actual = CatalogBuilder.build_catalog('test_data/pricat.csv', 'test_data/mappings.csv')

        with open('test_data/expected.json') as file:
            expected = json.load(file)
            self.maxDiff = None
            self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
