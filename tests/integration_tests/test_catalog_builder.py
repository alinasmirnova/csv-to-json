import json
import unittest
from src.catalog.catalog_builder import CatalogBuilder
from tests.helpers.test_data_path import get_test_data_path


class CatalogBuilderTestCase(unittest.TestCase):
    def test__build_catalog_integration_test(self):
        pricat_path_str = get_test_data_path('tests.integration_tests', 'pricat.csv')
        mapping_path_str = get_test_data_path('tests.integration_tests', 'mappings.csv')
        actual = CatalogBuilder.build_catalog(pricat_path_str, mapping_path_str)

        expected_path_str = get_test_data_path('tests.integration_tests', 'expected.json')
        with open(expected_path_str) as file:
            expected = json.load(file)
            self.maxDiff = None
            self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
