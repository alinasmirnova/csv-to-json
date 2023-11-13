import csv
from typing import List, Dict

from .exceptions import WrongFileFormatError


def read_csv(filename: str) -> List[Dict[str, str]]:
    parts = filename.split('.')
    if len(parts) < 2:
        raise ValueError('Wrong file name')

    extension = parts[-1]
    if extension != 'csv':
        raise WrongFileFormatError(f'.csv file expected but .{extension} file name found')

    def remove_none_key(obj):
        obj.pop(None, None)
        return obj

    with open(filename, encoding='utf-8') as file:
        return [obj for obj in map(remove_none_key, csv.DictReader(file, delimiter=';', restval=''))]
