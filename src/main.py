from src.fc.catalog.catalog_builder import CatalogBuilder
import pprint

mapping = input()
pricat = input()

res = CatalogBuilder.build_catalog(pricat_file_name=pricat, mappings_file_name=mapping)

print('Result catalog is:')
pprint.pprint(res)
