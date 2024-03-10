#!/usr/bin/python3

""" Unittest """

import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """ Review model test cases """
    def test_instance_attributes(self):
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_str_representation(self):
        """ Test string representation """
        review = Review()
        self.assertEqual(str(review), "[Review] ({}) {}".format(
            review.id, review.__dict__))

    def test_save_method(self):
        """ Test save() method """
        review = Review()
        initial_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(review.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """ Test to_dict() method """
        review = Review()
        obj_dict = review.to_dict()
        self.assertTrue('__class__' in obj_dict)
        self.assertTrue('created_at' in obj_dict)
        self.assertTrue('updated_at' in obj_dict)
        self.assertTrue('place_id' in obj_dict)
        self.assertTrue('user_id' in obj_dict)
        self.assertTrue('text' in obj_dict)

        self.assertEqual(obj_dict['__class__'], 'Review')
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertEqual(obj_dict['place_id'], "")
        self.assertEqual(obj_dict['user_id'], "")
        self.assertEqual(obj_dict['text'], "")


if __name__ == '__main__':
    unittest.main()