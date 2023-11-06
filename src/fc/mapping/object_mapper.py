from typing import Dict, List

from src.fc.mapping.field_mappers import FieldMapper, AsIsFieldMapper
from src.fc.mapping.rule import Rule


class ObjectMapper:
    @staticmethod
    def map(objects: List[Dict[str, str]], rules: List[Rule]) -> List[Dict[str, str]]:
        if len(objects) == 0:
            return []

        mappers = ObjectMapper._create_field_mappers(rules, objects[0])
        result = []
        for obj in objects:
            new_obj = {}
            for mapper in mappers:
                key = mapper.get_key()
                value = mapper.get_value(obj)
                new_obj[key] = value
            result.append(new_obj)
        return result

    @staticmethod
    def __flatten_keys(tuple_dict: Dict[tuple, FieldMapper]) -> set[str]:
        result = set()
        for key in tuple_dict:
            for val in key:
                result.add(val)
        return result

    @staticmethod
    def _create_field_mappers(rules: List[Rule], sample: Dict[str, str]) -> List[FieldMapper]:
        mappers_by_field = dict()

        for rule in rules:
            if rule.sourceType not in mappers_by_field:
                mappers_by_field[rule.sourceType] = rule.create_mapper()
            rule.append_to_mapper(mappers_by_field[rule.sourceType])

        fields_with_mappers = ObjectMapper.__flatten_keys(mappers_by_field)
        mappers = list(mappers_by_field.values())

        for field_name in sample:
            if field_name in fields_with_mappers:
                continue
            mappers.append(AsIsFieldMapper(field_name))

        return mappers
