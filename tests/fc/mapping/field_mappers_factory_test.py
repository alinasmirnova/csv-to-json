import unittest

from src.fc.mapping.field_mappers import AsIsFieldMapper, OneToOneFieldMapper, JoinManyToOneFieldMapper, ManyToOneFieldMapper
from src.fc.mapping.field_mappers_factory import create_mappers
from src.fc.mapping.rule import Rule


class FieldMappersFactoryTestCase(unittest.TestCase):

    def test__create_mappers(self):
        def create_rule(source, destination, sourceType, destinationType):
            return Rule({'source': source, 'destination': destination, 'source_type': sourceType,
                         'destination_type': destinationType})

        rules = [
            create_rule('winter', 'Winter', 'season', 'season'),
            create_rule('summer', 'Summer', 'season', 'season'),
            create_rule('EU|36', 'European size 36', 'size_group_code|size_code', 'size'),
            create_rule('EU|37', 'European size 37', 'size_group_code|size_code', 'size'),
            create_rule('', '', 'join1|join2', 'joined'),
                 ]
        sample = {
            'season': 'some text',
            'size_group_code': 'some text',
            'size_code': 'some text',
            'join1': 'some text',
            'join2': 'some text',
            'without_a_rule1': 'some text',
            'without_a_rule2': 'some text'
        }

        actual = create_mappers(rules, sample)

        expected = [AsIsFieldMapper('without_a_rule1'),
                    AsIsFieldMapper('without_a_rule2'),
                    OneToOneFieldMapper('season', 'season', {'winter': 'Winter', 'summer': 'Summer'}),
                    JoinManyToOneFieldMapper(('join1', 'join2'), 'joined'),
                    ManyToOneFieldMapper(('size_group_code', 'size_code'), 'size',
                                         {('EU', '36'): 'European size 36', ('EU', '37'): 'European size 37'})]

        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
