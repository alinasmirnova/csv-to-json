import unittest

from src.mapping.field_mappers import AsIsFieldMapper, OneToOneFieldMapper, JoinManyToOneFieldMapper, ManyToOneFieldMapper


class AsIsFieldMapperTestCase(unittest.TestCase):
    def setUp(self):
        self.mapper = AsIsFieldMapper('key')

    def test__get_key(self):
        self.assertEqual('key', self.mapper.get_key())

    def test__get_value__not_exist__raise(self):
        with self.assertRaises(KeyError):
            self.mapper.get_value({'unknownKey': 'value'})

    def test__get_value(self):
        self.assertEqual('value', self.mapper.get_value({'key': 'value'}))


class OneToOneFieldMapperTestCase(unittest.TestCase):
    def setUp(self):
        self.mapper = OneToOneFieldMapper('source', 'destination')
        self.mapper.add_values_map('value', 'VALUE')

    def test__get_key(self):
        self.assertEqual('destination', self.mapper.get_key())

    def test__get_value__not_exist__raise(self):
        with self.assertRaises(KeyError):
            self.mapper.get_value({'unknownKey': 'value'})

    def test__get_value__with_mapping(self):
        self.assertEqual('VALUE', self.mapper.get_value({'source': 'value'}))

    def test__get_value__without_mapping(self):
        self.assertEqual('unknown value', self.mapper.get_value({'source': 'unknown value'}))


class JoinManyToOneFieldMapperTestCase(unittest.TestCase):
    def setUp(self):
        self.mapper = JoinManyToOneFieldMapper(('source1', 'source2'), 'destination')

    def test__get_key(self):
        self.assertEqual('destination', self.mapper.get_key())

    def test__get_value__source_key_is_missing__raise(self):
        with self.assertRaises(KeyError):
            self.mapper.get_value({'unknownKey': 'value'})

    def test__get_value__with_join(self):
        self.assertEqual('value1 value2', self.mapper.get_value({'source1': 'value1', 'source2': 'value2'}))


class ManyToOneFieldMapperTestCase(unittest.TestCase):
    def setUp(self):
        self.mapper = ManyToOneFieldMapper(('source1', 'source2'), 'destination')
        self.mapper.add_values_map(('value1', 'value2'), 'NEW VALUE')

    def test__get_key(self):
        self.assertEqual('destination', self.mapper.get_key())

    def test__get_value__source_key_is_missing__raise(self):
        with self.assertRaises(KeyError):
            self.mapper.get_value({'unknownKey': 'value'})

    def test__get_value__unknown_value(self):
        with self.assertRaises(KeyError):
            self.mapper.get_value({'source1': 'unknown value', 'source2': 'value2'})

    def test__get_value__with_mapping(self):
        self.assertEqual('NEW VALUE', self.mapper.get_value({'source1': 'value1', 'source2': 'value2'}))


if __name__ == '__main__':
    unittest.main()
