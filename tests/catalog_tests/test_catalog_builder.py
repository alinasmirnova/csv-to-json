import json
import unittest
from src.catalog.catalog import Variation
from src.catalog.catalog_builder import CatalogBuilder
from tests.helpers.test_data_path import get_test_data_path


class CatalogBuilderTestCase(unittest.TestCase):
    def test__build_catalog_empty_list_raise(self):
        with self.assertRaises(ValueError):
            CatalogBuilder._build_catalog([])

    def test__build_catalog(self):
        objects = [
            {
                'brand': 'Via Vai',
                'article_number': '1',
                'season': 'winter',
                'name': 'coat'
            },
            {
                'brand': 'Via Vai',
                'article_number': '1',
                'season': 'winter',
                'name': 'shirt'
            },
            {
                'brand': 'Via Vai',
                'article_number': '2',
                'season': 'winter',
                'name': 'shirt'
            },
            {
                'brand': 'Via Vai',
                'article_number': '3',
                'season': 'autumn',
                'name': 'shirt'
            },
            {
                'brand': 'Via Vai',
                'article_number': '3',
                'season': 'spring',
                'name': 'coat'
            }
        ]

        actual = CatalogBuilder._build_catalog(list(map(Variation, objects)))
        expected = {
            'brand': 'Via Vai',
            'Articles': [
                {
                    'article_number': '1',
                    'season': 'winter',
                    'Variations': [
                        {
                            'name': 'coat'
                        },
                        {
                            'name': 'shirt'
                        },
                    ]
                },
                {
                    'article_number': '2',
                    'season': 'winter',
                    'name': 'shirt'
                },
                {
                    'article_number': '3',
                    'Variations': [
                        {
                            'season': 'autumn',
                            'name': 'shirt'
                        },
                        {
                            'season': 'spring',
                            'name': 'coat'
                        }
                    ]
                }
            ]
        }

        self.assertEqual(expected, actual)

    def test__build_catalog_integration_test(self):
        pricat_path_str = get_test_data_path('tests.catalog_tests', 'pricat.csv')
        mapping_path_str = get_test_data_path('tests.catalog_tests', 'mappings.csv')
        actual = CatalogBuilder.build_catalog(pricat_path_str, mapping_path_str)

        expected_path_str = get_test_data_path('tests.catalog_tests', 'expected.json')
        with open(expected_path_str) as file:
            expected = json.load(file)
            self.maxDiff = None
            self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
