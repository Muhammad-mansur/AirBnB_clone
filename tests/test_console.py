#!/usr/bin/python3

""" Unittest """

import unittest
from unittest.mock import patch, MagicMock, call, ANY
from models import storage
from models.user import User
from console import HBNBCommand
from io import StringIO  # For simulating user input


class TestHBNBCommand(unittest.TestCase):
    """ Test HBNB command """

    def tearDown(self):
        """ Clean up storage after each test """
        storage.reset()
        super().tearDown()

    @patch('sys.stdout')
    def test_quit(self, mock_stdout):
        command = HBNBCommand()
        command.do_quit('')
        self.assertEqual(mock_stdout.write.call_count, 0)

    def test_EOF(self):
        """ Test End of File """
        command = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            self.assertTrue(command.do_EOF(""))
            self.assertEqual(mock_stdout.write.call_count, 1)

    def test_emptyline(self):
        """ Test Empty Line """
        command = HBNBCommand()
        self.assertIsNone(command.emptyline())

    @patch('models.storage.new')
    @patch('models.storage.save')
    def test_create_valid_class(self, mock_save, mock_new):
        """ Test valid class creation """
        command = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            command.do_create("User")
            mock_stdout.getvalue().strip()

    @patch('sys.stdout')
    def test_create_invalid_class(self, mock_stdout):
        """ Test invalid class creation """
        command = HBNBCommand()
        command.do_create("InvalidClass")
        expected_calls = [call("** class doesn't exist **"), call('\n')]
        mock_stdout.write.assert_has_call(expected_calls)
        self.assertEqual(mock_stdout.write.call_count, 2)

    @patch('sys.stdout')
    def test_create_no_class(self, mock_stdout):
        """ Test no class creation """
        command = HBNBCommand()
        command.do_create("")
        expected_calls = [call("** class namw missing **\n"), call('\n')]
        mock_stdout.write.assert_called_has_calls(expected_calls)
        self.assertEqual(mock_stdout.write.call_count, 2)

    @patch('sys.stdout')
    def test_show_valid_args(self, mock_stdout):
        """ Test valid args """
        user = User(email="test@example.com", password="password")
        user.save()
        command = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            command.do_show("User {}".format(user.id))
            self.assertEqual(mock_stdout.write.call_count, 1)
        storage.all().pop("User.{}".format(user.id))  # Cleanup

    @patch('sys.stdout')
    def test_show_invalid_class(self, mock_stdout):
        """ Test invalid class """
        command = HBNBCommand()
        command.do_show("InvalidClass 1")
        expected_calls = [call("** class doesn't exist **"), call('\n')]
        mock_stdout.write.assert_has_calls(expected_calls)
        self.assertEqual(mock_stdout.write.call_count, 2)

    @patch('sys.stdout')
    def test_show_no_class(self, mock_stdout):
        """ Test no class """
        command = HBNBCommand()
        command.do_show("")
        expected_calls = [call("** class name missing **"), call('\n')]
        mock_stdout.write.assert_has_calls(expected_calls)
        self.assertEqual(mock_stdout.write.call_count, 2)

    @patch('sys.stdout')
    def test_show_no_id(self, mock_stdout):
        """ Test no id """
        command = HBNBCommand()
        command.do_show("User")
        expected_calls = [call("** instance id missing **"), call('\n')]
        mock_stdout.write.assert_has_calls(expected_calls)
        self.assertEqual(mock_stdout.write.call_count, 2)

    @patch('sys.stdout')
    def test_show_no_instance(self, mock_stdout):
        """ Test no instance """
        command = HBNBCommand()
        command.do_show("User 123")

    @patch('models.storage.delete')
    @patch('models.storage.save')
    def test_destroy_valid_args(self, mock_save, mock_delete):
        """ Test destroy valid arguments """
        user = User(email="test@example.com", password="password")
        user.save()
        command = HBNBCommand()
        command.do_destroy("User {}".format(user.id))
        mock_delete.assert_called_once_with("User.{}".format(user.id))
        mock_save.assert_called_once()


if __name__ == '__main__':
    unittest.main()
