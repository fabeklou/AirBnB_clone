#!/usr/bin/python3

"""entry point of the HBNB command interpreter"""

import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import shlex
import sys

implemented_classes = ["BaseModel", "User", "State",
                       "City", "Amenity", "Place", "Review"]
"""module level variable, holding the list of classes
that the user can create an instance of
"""


def handle_cmd_with_two_args(*tokens):
    """handle_cmd_with_two_args: checks the user input and
    prints the appropriate error messsage or perform the
    intended action

    Args:
        (tokens): list of arguments passed to the command

    Returns:
        (int): 0 if the command is complete
        (int): 1 if the command is incomplete or false

    """

    if not tokens:
        print("{}".format("** class name missing **"))
        return 1

    if tokens[0] not in implemented_classes:
        print("{}".format("** class doesn't exist **"))
        return 1

    if len(tokens) < 2:
        print("{}".format("** instance id missing **"))
        return 1

    return 0


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

    def do_quit(self, line):
        """quit: exits from the command interpreter"""
        sys.exit(0)

    def do_EOF(self, line):
        """EOF: exits from the command interpreter"""
        return True

    def emptyline(self):
        """emptyline: executes when the command is an empty
        line or white space (nothing is done)
        """
        return

    def do_create(self, line):
        """create: creates a new BaseModel object and saves it
        to the file_storage
        """
        if not line:
            print("{}".format("** class name missing **"))
            return

        if line == "BaseModel":
            obj = BaseModel()
        elif line == "User":
            obj = User()
        elif line == "State":
            obj = State()
        elif line == "City":
            obj = City()
        elif line == "Amenity":
            obj = Amenity()
        elif line == "Place":
            obj = Place()
        elif line == "Review":
            obj = Review()
        else:
            print("{}".format("** class doesn't exist **"))
            return

        obj.save()
        print("{}".format(obj.id))

    def do_show(self, line):
        """show: prints the string representation of an
        instance based on the class name and id
        """

        # split the command (line) using shell-like syntax
        tokens: list[str] = shlex.split(line)

        # do nothing else if the user input is incomplete or false
        if handle_cmd_with_two_args(*tokens):
            return

        key: str = "{}.{}".format(tokens[0], tokens[1])
        objects: dict = storage.all()

        if key in objects:
            print(objects[key])
            return

        print("{}".format("** no instance found **"))

    def do_destroy(self, line):
        """destroy: deletes an instance based on the class name
        and id, then saves the change into the JSON file
        """

        # split the command (line) using shell-like syntax
        tokens: list[str] = shlex.split(line)

        # do nothing else if the user input is incomplete or false
        if handle_cmd_with_two_args(*tokens):
            return

        key: str = "{}.{}".format(tokens[0], tokens[1])
        objects: dict = storage.all()

        if key in objects:
            del objects[key]
            storage.save()
            return

        print("{}".format("** no instance found **"))

    def do_all(self, line):
        """all: prints all string representation of all instances
        based or not on the class name
        """
        str_rep_list: str = []
        objects: dict = storage.all()

        if not line:
            for key, obj in objects.items():
                str_rep_list.append(str(obj))
            print(str_rep_list)
        else:
            if line not in implemented_classes:
                print("{}".format("** class doesn't exist **"))
                return

            for key, obj in objects.items():
                if obj.__class__.__name__ == line:
                    str_rep_list.append(str(obj))
            print(str_rep_list)

    def do_update(self, line):
        """update: updates an instance based on the class name
        and id by adding or updating attribute and then save
        the change into the JSON file

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        # split the command (line) using shell-like syntax
        tokens: list[str] = shlex.split(line)

        # do nothing else if the user input is incomplete or false
        if handle_cmd_with_two_args(*tokens[0:2]):
            return

        key: str = "{}.{}".format(tokens[0], tokens[1])
        objects: dict = storage.all()

        if key not in objects:
            print("{}".format("** no instance found **"))
            return

        if len(tokens) < 3:
            print("{}".format("** attribute name missing **"))
            return

        if len(tokens) < 4:
            print("{}".format("** value missing **"))
            return

        attr_name, attr_value = tokens[2:4]
        try:
            attr_value = json.loads(attr_value)
        except Exception:
            pass

        setattr(objects[key], attr_name, attr_value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
