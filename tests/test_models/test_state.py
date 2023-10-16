#!/usr/bin/python3

"""This module defines a TestState class, which is used to
test the State class form the models package
"""

from models.state import State
import unittest


class TestState(unittest.TestCase):
    """Defines test cases for State class"""

    # Show the whole output when an assert method fails
    maxDiff = None

    def test_state_class(self):
        """creats and test a new state object"""
        so00 = State()

        self.assertEqual(so00.__class__.__name__, "State")
        self.assertTrue(hasattr(so00, "id"))
        self.assertEqual(so00.created_at, so00.updated_at)
        self.assertTrue(hasattr(so00, "name"))

    def test_name(self):
        """tests the public class attribute name"""
        so01 = State()

        if hasattr(so01, "name"):
            self.assertEqual(so01.name, "")
            setattr(so01, "name", "TOGO")
        self.assertEqual(so01.name, "TOGO")
