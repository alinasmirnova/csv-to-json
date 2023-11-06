from __future__ import annotations

from typing import Dict, List


class GroupingObject:
    def __init__(self):
        self.children = []
        self.common_fields = {}

    def _add_child(self, obj: Dict[str, str]):
        def differs_from_obj(pair):
            key, value = pair
            return key in obj and obj[key] == value

        if len(self.children) == 0:
            self.common_fields = obj.copy()
        else:
            self.common_fields = dict(filter(differs_from_obj, self.common_fields.items()))

        self.children.append(obj)

    def _to_dictionary(self, children_field_name):
        def remove_common(obj):
            result = obj.copy()
            for field in self.common_fields:
                del result[field]
            return result

        res = self.common_fields.copy()
        elements = list(map(remove_common, self.children))
        if len(elements) > 0 and len(elements[0]) > 0:
            res[children_field_name] = elements

        return res
