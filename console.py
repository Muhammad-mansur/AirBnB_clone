#!/usr/bin/python3

"""import cmd module"""


import cmd
import models
from models.base_model import BaseModel
from models import storage


__classes_list = ["BaseModel", "User"]


class HBNBCommand(cmd.Cmd):
    """This class defines the interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """This defines quitting command to qxit the program"""
        return True

    def do_EOF(self, arg):
        """This defines the condition to quit when encountered with EOF"""
        print()
        return True

    def emptyline(self):
        """Override method to ensure empty lines"""
        pass

    def do_create(self, arg):
        """Create a new instance"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exsit **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
