#!/usr/bin/python3
"""import cmd module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class defines the interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """This defines quitting command to qxit the program"""
        reture True

    def do_EOF(self, arg):
        """This defines the condition to quit when encountered with EOF"""
        print()
        reture True

    def emptyline(self):
        """Override method to ensure empty lines"""
        pass


if __name__ == '__main__':
    HBNBCommand()cmdloop()
