#!/usr/bin/python3

""" Unittest """

import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Base Model Test Cases """
    def setUp(self):
        """ """
        pass

    def test_no_args(self):
        """ Test creation with no arguments """
        obj = BaseModel()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_with_args(self):
        """ Test creation with arguments """
        obj = BaseModel(
                id='123', created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now())
        self.assertEqual(obj.id, '123')

    def test_str_representation(self):
        """ Test string representation """
        obj = BaseModel()
        obj_str = str(obj)
        self.assertEqual('[BaseModel]' in obj_str)
        self.assertEqual('id=' in obj_str)

    def test_save_method(self):
        """ Test save method """
        obj = BaseModel()
        ini_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, ini_updated_at)

    def test_to_dict_method(self):
        """ Test to_dict() method """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue('_class__' in obj_dict)
        self.asserTrue('created_at' in obj_dict)
        self.asserTrue('updated_at' in obj_dict)

        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
