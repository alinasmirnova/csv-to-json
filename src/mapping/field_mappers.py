from __future__ import annotations

from abc import abstractmethod
from dataclasses import dataclass, field
from typing import Dict


class FieldMapper:
    @abstractmethod
    def get_key(self) -> str:
        pass

    @abstractmethod
    def get_value(self, obj: Dict[str, str]) -> str:
        pass


class ConditionalFieldMapper(FieldMapper):
    @abstractmethod
    def add_values_map(self, old: str | tuple, new: str) -> None:
        pass


@dataclass
class AsIsFieldMapper(FieldMapper):
    key: str

    def get_key(self) -> str:
        return self.key

    def get_value(self, obj: Dict[str, str]) -> str:
        return obj[self.key]


@dataclass
class OneToOneFieldMapper(ConditionalFieldMapper):
    sourceType: str
    destinationType: str
    values: dict = field(default_factory=dict)

    def get_key(self) -> str:
        return self.destinationType

    def get_value(self, obj: Dict[str, str]) -> str:
        return self.values.get(obj[self.sourceType], obj[self.sourceType])

    def add_values_map(self, old: str, new: str) -> None:
        self.values[old] = new


@dataclass
class JoinManyToOneFieldMapper(FieldMapper):
    sourceTypes: tuple
    destinationType: str

    def get_key(self) -> str:
        return self.destinationType

    def get_value(self, obj: Dict[str, str]) -> str:
        return ' '.join([obj[key] for key in self.sourceTypes])


@dataclass
class ManyToOneFieldMapper(ConditionalFieldMapper):
    sourceTypes: tuple
    destinationType: str
    values: dict = field(default_factory=dict)

    def get_key(self) -> str:
        return self.destinationType

    def get_value(self, obj: Dict[str, str]) -> str:
        key = tuple(obj[sourceKey] for sourceKey in self.sourceTypes)
        return self.values[key]

    def add_values_map(self, old: tuple, new: str) -> None:
        self.values[old] = new
