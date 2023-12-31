import pprint

from src.catalog.catalog_builder import CatalogBuilder

print('Input full path to mapping.csv file:')
mapping = input()

print('Input full path to pricat.csv file:')
pricat = input()

res = CatalogBuilder.build_catalog(pricat_file_name=pricat, mappings_file_name=mapping)

print('Result catalog_tests is:')
pprint.pprint(res)
