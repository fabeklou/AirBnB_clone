#!/usr/bin/python3

"""This module defines a TestHBNBCommand class, which is used to
test the HBNBCommand class (sub_class of the Cmd) which defines
the console features and behavior
"""

from console import HBNBCommand
import unittest


class TestHBNBCommand(unittest.TestCase):
    """Defines test cases for TestHBNBCommand class"""

    # Show the whole output when an assert method fails
    maxDiff = None

    def test_new_command(self):
        pass
