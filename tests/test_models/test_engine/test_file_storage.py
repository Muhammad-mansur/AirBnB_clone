#!/usr/bin/python3

""" Unittest """

import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ File storage test case """
    def setUp(self):
        """ Set up """
        self.test_storage = FileStorage()

    @patch('os.path.exists')
    def test_reload_no_file(self, mock_exists):
        """ check if path exists """
        mock_exists.return_value = False
        self.test_storage.reload()
        self.assertEqual(self.test_storage.all(), {})

    def test_reload_empty_file(self):
        """ check for empty line """
        with open('file.json', 'w') as f:
            f.write('{}')
        self.test_storage.reload()
        self.assertEqual(self.test_storage.all(), {})
        os.remove('file.json')  # Cleanup

    def test_reload_with_data(self):
        """ check for data reload """
        user = User(email="test@example.com", password="password")
        self.test_storage.new(user)
        self.test_storage.save()

        self.test_storage = FileStorage()  # Re-initialize
        self.test_storage.reload()

        objects = self.test_storage.all()
        self.assertEqual(len(objects), 1)
        self.assertIsInstance(list(objects.values())[0], User)
        os.remove('file.json')  # Cleanup

    def test_new_and_save(self):
        """ check for new() and save() """
        user = User(email="test@example.com", password="password")
        self.test_storage.new(user)
        self.test_storage.save()

        with open('file.json', 'r') as f:
            loaded_objects = json.load(f)

        self.assertEqual(len(loaded_objects), 1)
        self.assertEqual(loaded_objects[
            f"{user.__class__.__name__}.{user.id}"]["email"], user.email)
        os.remove('file.json')  # Cleanup

    def test_all(self):
        """ test """
        user = User(email="test@example.com", password="password")
        self.test_storage.new(user)
        self.assertEqual(self.test_storage.all(), {
            f"{user.__class__.__name__}.{user.id}": user})

    def test_new_with_none(self):
        """ new with none """
        with self.assertRaises(AttributeError):
            self.test_storage.new(None)

    def test_save_empty_objects(self):
        """ save_empty """
        self.test_storage.save()
        with open('file.json', 'r') as f:
            loaded_objects = json.load(f)
        self.assertEqual(loaded_objects, {})
        os.remove('file.json')  # Cleanup


if __name__ == '__main__':
    unittest.main()
