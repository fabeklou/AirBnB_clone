#!/usr/bin/python3

"""This module defines a TestPlace class, which is used to
test the Place class form the models package
"""

from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Defines test cases for Place class"""

    # Show the whole output when an assert method fails
    maxDiff = None

    def test_place_class(self):
        """creats and test a new user object"""
        po00 = Place()

        self.assertEqual(po00.__class__.__name__, "Place")
        self.assertTrue(hasattr(po00, "id"))
        self.assertEqual(po00.created_at, po00.updated_at)
        self.assertTrue(hasattr(po00, "city_id"))
        self.assertTrue(hasattr(po00, "user_id"))
        self.assertTrue(hasattr(po00, "name"))
        self.assertTrue(hasattr(po00, "description"))

        self.assertTrue(hasattr(po00, "number_rooms"))
        self.assertTrue(hasattr(po00, "number_bathrooms"))
        self.assertTrue(hasattr(po00, "max_guest"))
        self.assertTrue(hasattr(po00, "price_by_night"))

        self.assertTrue(hasattr(po00, "latitude"))
        self.assertTrue(hasattr(po00, "longitude"))

        self.assertTrue(hasattr(po00, "amenity_ids"))

    def test_city_id(self):
        """tests the public class attribute city_id"""
        po01 = Place()

        if hasattr(po01, "city_id"):
            self.assertEqual(po01.city_id, "")
            setattr(po01, "city_id", "c79f66ed-d9d4-4883-b1bf-e53748edbc63")
        self.assertEqual(po01.city_id, "c79f66ed-d9d4-4883-b1bf-e53748edbc63")

    def test_user_id(self):
        """tests the public class attribute user_id"""
        po02 = Place()

        if hasattr(po02, "user_id"):
            self.assertEqual(po02.user_id, "")
            setattr(po02, "user_id", "e790a4a1-bd05-46e5-ac30-4b8f18a5c96e")
        self.assertEqual(po02.user_id, "e790a4a1-bd05-46e5-ac30-4b8f18a5c96e")

    def test_name(self):
        """tests the public class attribute name"""
        po03 = Place()

        if hasattr(po03, "name"):
            self.assertEqual(po03.name, "")
            setattr(po03, "name", "Heaven")
        self.assertEqual(po03.name, "Heaven")

    def test_description(self):
        """tests the public class attribute description"""
        po04 = Place()

        if hasattr(po04, "description"):
            self.assertEqual(po04.description, "")
            setattr(po04, "description", "This a short description")
        self.assertEqual(po04.description, "This a short description")

    def test_number_rooms(self):
        """tests the public class attribute number_rooms"""
        po05 = Place()

        if hasattr(po05, "number_rooms"):
            self.assertEqual(po05.number_rooms, 0)
            setattr(po05, "number_rooms", 3)
        self.assertEqual(po05.number_rooms, 3)

    def test_number_bathrooms(self):
        """tests the public class attribute number_bathrooms"""
        po06 = Place()

        if hasattr(po06, "number_bathrooms"):
            self.assertEqual(po06.number_bathrooms, 0)
            setattr(po06, "number_bathrooms", 2)
        self.assertEqual(po06.number_bathrooms, 2)

    def test_max_guest(self):
        """tests the public class attribute max_guest"""
        po07 = Place()

        if hasattr(po07, "max_guest"):
            self.assertEqual(po07.max_guest, 0)
            setattr(po07, "max_guest", 5)
        self.assertEqual(po07.max_guest, 5)

    def test_price_by_night(self):
        """tests the public class attribute price_by_night"""
        po08 = Place()

        if hasattr(po08, "price_by_night"):
            self.assertEqual(po08.price_by_night, 0)
            setattr(po08, "price_by_night", 35)
        self.assertEqual(po08.price_by_night, 35)

    def test_latitude(self):
        """tests the public class attribute latitude"""
        po09 = Place()

        if hasattr(po09, "latitude"):
            self.assertEqual(po09.latitude, 0.0)
            setattr(po09, "latitude", 98.230003)
        self.assertEqual(po09.latitude, 98.230003)

    def test_longitude(self):
        """tests the public class attribute longitude"""
        po10 = Place()

        if hasattr(po10, "longitude"):
            self.assertEqual(po10.longitude, 0.0)
            setattr(po10, "longitude", -21.450001)
        self.assertEqual(po10.longitude, -21.450001)

    def test_amenity_ids(self):
        """tests the public class attribute amenity_ids"""
        po10 = Place()

        if hasattr(po10, "amenity_ids"):
            self.assertEqual(po10.amenity_ids, [])
            setattr(po10, "amenity_ids", [
                    "24114577-293c-401e-9a0b-6eefeca6bfd5",
                    "a0eaded2-8285-4c6c-9d05-9fb155a494c0"])
        self.assertEqual(po10.amenity_ids, [
            "24114577-293c-401e-9a0b-6eefeca6bfd5",
            "a0eaded2-8285-4c6c-9d05-9fb155a494c0"])
