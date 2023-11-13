from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from .field_mappers import FieldMapper, JoinManyToOneFieldMapper, ManyToOneFieldMapper, OneToOneFieldMapper, \
    ConditionalFieldMapper


@dataclass
class Rule:
    source: tuple
    destination: str
    sourceType: tuple
    destinationType: str
    delimiter: str

    def __init__(self, values: Dict[str, str]):
        def get_delimiter(s):
            sym = '|'
            if sym in s:
                return sym
            return ''

        def parse(s, delimiter):
            if delimiter == '' or delimiter not in s:
                return (s,)

            return tuple(s.split(delimiter))

        self.delimiter = get_delimiter(values['source_type'])
        self.source = parse(values['source'], self.delimiter)
        self.destination = values['destination']
        self.sourceType = parse(values['source_type'], self.delimiter)
        self.destinationType = values['destination_type']

    def create_mapper(self) -> FieldMapper:
        if self.delimiter == '|' and self.source == ('',) and self.destination == '':
            return JoinManyToOneFieldMapper(self.sourceType, self.destinationType)

        if self.delimiter == '|':
            return ManyToOneFieldMapper(self.sourceType, self.destinationType)

        return OneToOneFieldMapper(self.sourceType[0], self.destinationType)

    def append_to_mapper(self, mapper: FieldMapper):
        if isinstance(mapper, OneToOneFieldMapper):
            mapper.add_values_map(self.source[0], self.destination)
        elif isinstance(mapper, ConditionalFieldMapper):
            mapper.add_values_map(self.source, self.destination)
