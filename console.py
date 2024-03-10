#!/usr/bin/python3
"""import cmd module"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """This class defines the interpreter"""
    prompt = '(hbnb) '
    __classes_list = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

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
        elif arg not in HBNBCommand.__classes_list:
            print("** class doesn't exsit **")
        else:
            new_instance = globals()[arg]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string rep of an instance"""
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes_list:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(args[0], args[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        args = arg.split()
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        elif args[0] not in HBNBCommand.__classes_list:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string rep of all instances"""
        args = arg.split()
        instances = []

        if not args:
            for obj in storage.all().values():
                instances.append(str(obj))
        elif args[0] not in HBNBCommand.__classes_list:
            print("** class doesn't exist **")
            return
        else:
            for key, obj in storage.all().items():
                if args[0] in key:
                    instances.append(str(obj))

        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split(" ")

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes_list:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[key]
        setattr(instance, args[2], args[3])
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
