from src.fc.catalog.catalog import Catalog, Variation, Article
from typing import Dict, List

from src.fc.io.csv_reader import read_csv
from src.fc.mapping.object_mapper import ObjectMapper
from src.fc.mapping.rule import Rule


class CatalogBuilder:
    @staticmethod
    def _build_catalog(objects: List[Variation]) -> Dict:
        if len(objects) == 0:
            raise ValueError("Can't create catalog without variations")

        articles = {}
        for obj in objects:
            article_number = obj.get_article_number()
            if article_number in articles:
                articles[article_number].add_variation(obj)
            else:
                articles[article_number] = Article(obj)

        catalog = Catalog()
        for article in articles.values():
            catalog.add_article(article)

        return catalog.to_dictionary()

    @staticmethod
    def build_catalog(pricat_file_name: str, mappings_file_name: str) -> Dict:
        pricat = read_csv(pricat_file_name)
        mappings = read_csv(mappings_file_name)

        rules = list(map(Rule, mappings))

        elements = list(map(Variation, ObjectMapper.map(pricat, rules)))

        return CatalogBuilder._build_catalog(elements)
