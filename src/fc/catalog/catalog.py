from __future__ import annotations


from typing import Dict, List
from src.fc.grouping.grouping_object import GroupingObject


class Variation(dict):
    def get_article_number(self):
        return self['article_number']


class Article(GroupingObject):
    def __init__(self, obj: Variation):
        super().__init__()
        self.article_number = obj['article_number']
        self.add_variation(obj)

    def add_variation(self, variation: Variation):
        if variation.get_article_number() != self.article_number:
            raise ValueError("Can't add variation from another article")

        self._add_child(variation)

    def to_dictionary(self) -> Dict[str, str | List]:
        return self._to_dictionary('Variations')


class Catalog(GroupingObject):
    def add_article(self, article: Article):
        self._add_child(article.to_dictionary())

    def to_dictionary(self) -> Dict[str, str | List]:
        return self._to_dictionary('Articles')
