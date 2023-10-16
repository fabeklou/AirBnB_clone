#!/usr/bin/python3

"""This module defines a TestAmenity class, which is used to
test the Amenity class form the models package
"""

from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):
    """Defines test cases for Amenity class"""

    # Show the whole output when an assert method fails
    maxDiff = None

    def test_amenity_class(self):
        """creats and test a new Amenity object"""
        ao00 = Amenity()

        self.assertEqual(ao00.__class__.__name__, "Amenity")
        self.assertTrue(hasattr(ao00, "id"))
        self.assertEqual(ao00.created_at, ao00.updated_at)
        self.assertTrue(hasattr(ao00, "name"))

    def test_name(self):
        """tests the public class attribute name"""
        ao01 = Amenity()

        if hasattr(ao01, "name"):
            self.assertEqual(ao01.name, "")
            setattr(ao01, "name", "Internet")
        self.assertEqual(ao01.name, "Internet")
