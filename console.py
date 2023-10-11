#!/usr/bin/python3

"""entry point of the HBNB command interpreter"""

import cmd
from models.base_model import BaseModel
from models import storage
import sys


class HBNBCommand(cmd.Cmd):
    """Defines the behavior and functionalities
    of the HBNB Consol

    """
    prompt: str = "(hbnb) "
    """str: prompt asking for the user to type a command"""

    message = "Welcome to hbnb console, built for debugging and testing !"
    line = "\n=========================================================="
    intro: str = message + line
    """str: airbnb console welcome message"""

    def do_quit(self, arg):
        """quit: exits from the command interpreter"""
        sys.exit(0)

    def do_EOF(self, arg):
        """EOF: exits from the command interpreter"""
        sys.exit(0)

    def emptyline(self):
        """emptyline: executes when the command is an empty line"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
