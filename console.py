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

    def do_show(self, arg):
        """Prints the string rep of an instance"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
        elif arg != "BaseModel":
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(arg[0], arg[1])
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, arg):
        """Prints all string rep of all instances"""
        instances = []
        if not arg:
            if arg not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                if arg in key:
                    instances.append(str(obj))
        else:
            for obj in storage.all().values():
                instances.append(str(obj))

        print(instances)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split(" ")

        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in ["BaseModel"]:
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
