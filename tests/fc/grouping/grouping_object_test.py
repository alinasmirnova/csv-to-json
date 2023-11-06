import unittest

from src.fc.grouping.grouping_object import GroupingObject


class GroupingObjectTestCase(unittest.TestCase):
    def setUp(self):
        self.obj = {
            '1': '1',
            '2': '2',
            '3': '3'
        }
        self.grouping = GroupingObject(self.obj)

    def test__add_child__same_values__keep_grouping(self):
        obj2 = {
            '1': '1',
            '2': '2',
            '3': '3'
        }
        self.grouping._add_child(obj2)

        self.assertCountEqual([self.obj, obj2], self.grouping.children)
        self.assertCountEqual(self.obj, self.grouping.common_fields)

    def test__add_child__different_values__remove_common_value(self):
        obj2 = {
            '1': '1',
            '2': '2',
            '3': '4'
        }
        self.grouping._add_child(obj2)

        self.assertCountEqual([self.obj, obj2], self.grouping.children)
        self.assertCountEqual({'1': '1', '2': '2'}, self.grouping.common_fields)

    def test__add_child_new_field_raise(self):
        with self.assertRaises(KeyError):
            self.grouping._add_child({'1': '1', '2': '2'})


if __name__ == '__main__':
    unittest.main()
