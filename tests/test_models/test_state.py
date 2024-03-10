#!/usr/bin/python3

""" Unittest """

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ State model test cases """
    def test_instance_attributes(self):
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))
        self.assertEqual(state.name, "")

    def test_str_representation(self):
        """ Test string representation """
        state = State()
        self.assertEqual(str(state), "[State] ({}) {}".format(
            state.id, state.__dict__))

    def test_save_method(self):
        """ Test save() method """
        state = State()
        initial_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(state.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """ Test to_dict() method """
        state = State()
        obj_dict = state.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('name' in obj_dict)

        self.assertEqual(obj_dict['__class__'], 'State')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertEqual(obj_dict['name'], "")


if __name__ == '__main__':
    unittest.main()