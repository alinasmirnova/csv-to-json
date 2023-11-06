from typing import Dict, List, Set
from src.fc.mapping.field_mappers import *
from src.fc.mapping.rule import Rule


def flatten_keys(tuple_dict: Dict[tuple, FieldMapper]) -> set[str]:
    result = set()
    for key in tuple_dict:
        for val in key:
            result.add(val)

    return result


def create_mappers(rules: List[Rule], sample: Dict[str, str]) -> List[FieldMapper]:
    mappers_by_field = dict()

    for rule in rules:
        if rule.sourceType not in mappers_by_field:
            mappers_by_field[rule.sourceType] = rule.create_mapper()
        rule.append_to_mapper(mappers_by_field[rule.sourceType])

    fields_with_mappers = flatten_keys(mappers_by_field)

    mappers = list(mappers_by_field.values())

    for field_name in sample:
        if field_name in fields_with_mappers:
            continue
        mappers.append(AsIsFieldMapper(field_name))

    return mappers
