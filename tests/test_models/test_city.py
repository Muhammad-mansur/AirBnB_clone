#!/usr/bin/python3

""" Unittest """

import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ City model test cases """
    def test_instance_attributes(self):
        """ Test instance attributes """
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_str_representation(self):
        """ Test string representation """
        city = City()
        self.assertEqual(str(city), "[City] ({}) {}".format(
            city.id, city.__dict__))

    def test_save_method(self):
        """ Test save method """
        city = City()
        initial_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(city.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """ Test to_dict() method """
        city = City()
        obj_dict = city.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('state_id' in obj_dict)
        self.assertTrue('name' in obj_dict)

        self.assertEqual(obj_dict['__class__'], 'City')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertEqual(obj_dict['state_id'], "")
        self.assertEqual(obj_dict['name'], "")


if __name__ == '__main__':
    unittest.main()
