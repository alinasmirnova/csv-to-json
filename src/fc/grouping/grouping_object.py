from __future__ import annotations

from typing import Dict, List


class GroupingObject:
    def __init__(self, obj: Dict[str, str | List]):
        self.children = [obj]
        self.common_fields = obj.copy()

    def _add_child(self, obj: Dict[str, str]):
        def differs_from_obj(pair):
            key, value = pair
            return obj[key] == value

        self.common_fields = dict(filter(differs_from_obj, self.common_fields.items()))
        self.children.append(obj)
