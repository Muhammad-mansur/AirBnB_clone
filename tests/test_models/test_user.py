#!/usr/bin/python3

""" Unittest """

import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Test cases for User model """

    def test_user_inherits_from_base_model(self):
        """ Test if User inherits from BaseModel """
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)
        
    def test_user_attributes(self):
        """ Test User attributes """
        new_user = User()
        self.assertTrue(hasattr(new_user, 'email'))
        self.assertTrue(hasattr(new_user, 'password'))
        self.assertTrue(hasattr(new_user, 'first_name'))
        self.assertTrue(hasattr(new_user, 'last_name'))
        
    def test_user_attribute_types(self):
        """ Test User attribute types """
        new_user = User()
        self.assertIsInstance(new_user.email, str)
        self.assertIsInstance(new_user.password, str)
        self.assertIsInstance(new_user.first_name, str)
        self.assertIsInstance(new_user.last_name, str)
        
    def test_user_attribute_default_values(self):
        """ Test User attribute default values """
        new_user = User()
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")
        
    def test_user_created_at_updated_at_types(self):
        """ Test User created_at and updated_at attributes types """
        new_user = User()
        self.assertIsInstance(new_user.created_at, datetime)
        self.assertIsInstance(new_user.updated_at, datetime)
        
    def test_user_str_method(self):
        """ Test User __str__ method """
        new_user = User()
        user_str = new_user.__str__()
        self.assertIsInstance(user_str, str)

    def test_user_to_dict_method(self):
        """ Test User to_dict method """
        new_user = User()
        user_dict = new_user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertTrue('__class__' in user_dict)
        self.assertTrue('created_at' in user_dict)
        self.assertTrue('updated_at' in user_dict)
        self.assertTrue('id' in user_dict)
        self.assertTrue('email' in user_dict)
        self.assertTrue('password' in user_dict)
        self.assertTrue('first_name' in user_dict)
        self.assertTrue('last_name' in user_dict)

    def test_user_to_dict_values(self):
        """ Test User to_dict method values """
        new_user = User()
        user_dict = new_user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(type(user_dict['created_at']), str)
        self.assertEqual(type(user_dict['updated_at']), str)
        self.assertEqual(type(user_dict['id']), str)
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")


if __name__ == '__main__':
    unittest.main()