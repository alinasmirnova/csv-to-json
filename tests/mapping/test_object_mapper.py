import unittest

from src.mapping.field_mappers import (AsIsFieldMapper, OneToOneFieldMapper, JoinManyToOneFieldMapper,
                                       ManyToOneFieldMapper)
from src.mapping.object_mapper import ObjectMapper
from src.mapping import Rule


class ObjectMapperTestCase(unittest.TestCase):
    def setUp(self):
        def create_rule(source, destination, source_type, destination_type):
            return Rule({'source': source, 'destination': destination, 'source_type': source_type,
                         'destination_type': destination_type})

        self.rules = [
            create_rule('winter', 'Winter', 'season', 'season'),
            create_rule('summer', 'Summer', 'season', 'season'),
            create_rule('EU|36', 'European size 36', 'size_group_code|size_code', 'size'),
            create_rule('EU|37', 'European size 37', 'size_group_code|size_code', 'size'),
            create_rule('', '', 'price_buy_net|currency', 'price'),
        ]

    def test__create_field_mappers(self):
        sample = {
            'season': 'some text',
            'size_group_code': 'some text',
            'size_code': 'some text',
            'price_buy_net': 'some text',
            'currency': 'some text',
            'without_a_rule1': 'some text',
            'without_a_rule2': 'some text'
        }

        actual = ObjectMapper._create_field_mappers(self.rules, sample)

        expected = [AsIsFieldMapper('without_a_rule1'),
                    AsIsFieldMapper('without_a_rule2'),
                    OneToOneFieldMapper('season', 'season', {'winter': 'Winter', 'summer': 'Summer'}),
                    JoinManyToOneFieldMapper(('price_buy_net', 'currency'), 'price'),
                    ManyToOneFieldMapper(('size_group_code', 'size_code'), 'size',
                                         {('EU', '36'): 'European size 36', ('EU', '37'): 'European size 37'})]

        self.assertCountEqual(expected, actual)

    def test__map_objects(self):
        objects = [
            {
                'season': 'winter',
                'size_group_code': 'EU',
                'size_code': '36',
                'price_buy_net': '58.5',
                'currency': 'EU',
                'name': 'Coat',
            },
            {
                'season': 'summer',
                'size_group_code': 'EU',
                'size_code': '37',
                'price_buy_net': '60',
                'currency': 'EU',
                'name': 'Shirt',
            },
        ]

        actual = ObjectMapper.map(objects, self.rules)
        expected = [
            {
                'season': 'Winter',
                'size': 'European size 36',
                'price': '58.5 EU',
                'name': 'Coat',
            },
            {
                'season': 'Summer',
                'size': 'European size 37',
                'price': '60 EU',
                'name': 'Shirt',
            },
        ]
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
