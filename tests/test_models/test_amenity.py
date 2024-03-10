#!/usr/bin/python3

""" Unittest """

import unittest
from unittest import TestCase
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Amenity model """
    def test_instance_attributes(self):
        """ Test instance attribute """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'id'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")

    def test_str_representation(self):
        """ Test string representaion """
        amenity = Amenity()
        self.assertEqual(str(amenity), "[Amenity] ({}) {}".format(
            amenity.id, amenity.__dict__))

    def test_save_method(self):
        """ Test save method """
        amenity = Amenity()
        initial_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(amenity.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """ Test dictionary """
        amenity = Amenity()
        obj_dict = amenity.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('name' in obj_dict)

        self.assertEqual(obj_dict['__class__'], 'Amenity')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertEqual(obj_dict['name'], "")


if __name__ == '__main__':
    unittest.main()
