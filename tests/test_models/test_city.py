#!/usr/bin/python3

"""This module defines a TestCity class, which is used to
test the City class form the models package
"""

from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Defines test cases for City class"""

    # Show the whole output when an assert method fails
    maxDiff = None

    def test_city_class(self):
        """creats and test a new city object"""
        co00 = City()

        self.assertEqual(co00.__class__.__name__, "City")
        self.assertTrue(hasattr(co00, "id"))
        self.assertEqual(co00.created_at, co00.updated_at)
        self.assertTrue(hasattr(co00, "state_id"))
        self.assertTrue(hasattr(co00, "name"))

    def test_state_id(self):
        """tests the public class attribute state_id"""
        co01 = City()

        if hasattr(co01, "state_id"):
            self.assertEqual(co01.state_id, "")
            setattr(co01, "state_id", "835e48a0-840c-4651-bb63-1224a1138760")
        self.assertEqual(co01.state_id, "835e48a0-840c-4651-bb63-1224a1138760")

    def test_name(self):
        """tests the public class attribute name"""
        co02 = City()

        if hasattr(co02, "name"):
            self.assertEqual(co02.name, "")
            setattr(co02, "name", "Lome la belle")
        self.assertEqual(co02.name, "Lome la belle")
