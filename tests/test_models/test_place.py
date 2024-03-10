#!/usr/bin/python3

""" Unittest """

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Place model test cases """

    def test_instance_attributes(self):
        """ Test instance attribute """
        place = Place()
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_str_representation(self):
        """ Test string representation """
        place = Place()
        self.assertEqual(str(place), "[Place] ({}) {}".format(
            place.id, place.__dict__))

    def test_save_method(self):
        """ Test save() method """
        place = Place()
        initial_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(place.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """ Test to_dict() """
        place = Place()
        obj_dict = place.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('city_id' in obj_dict)
        self.assertTrue('user_id' in obj_dict)
        self.assertTrue('name' in obj_dict)
        self.assertTrue('description' in obj_dict)
        self.assertTrue('number_rooms' in obj_dict)
        self.assertTrue('number_bathrooms' in obj_dict)
        self.assertTrue('max_guest' in obj_dict)
        self.assertTrue('price_by_night' in obj_dict)
        self.assertTrue('latitude' in obj_dict)
        self.assertTrue('longitude' in obj_dict)
        self.assertTrue('amenity_ids' in obj_dict)

        self.assertEqual(obj_dict['__class__'], 'Place')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertEqual(obj_dict['city_id'], "")
        self.assertEqual(obj_dict['user_id'], "")
        self.assertEqual(obj_dict['name'], "")
        self.assertEqual(obj_dict['description'], "")
        self.assertEqual(obj_dict['number_rooms'], 0)
        self.assertEqual(obj_dict['number_bathrooms'], 0)
        self.assertEqual(obj_dict['max_guest'], 0)
        self.assertEqual(obj_dict['price_by_night'], 0)
        self.assertEqual(obj_dict['latitude'], 0.0)
        self.assertEqual(obj_dict['longitude'], 0.0)
        self.assertEqual(obj_dict['amenity_ids'], [])


if __name__ == '__main__':
    unittest.main()
