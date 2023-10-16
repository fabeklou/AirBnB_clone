#!/usr/bin/python3

"""This module defines a TestUser class, which is used to
test the User class form the models package
"""

from models.user import User
import unittest


class TestUser(unittest.TestCase):
    """Defines test cases for User class"""

    # Show the whole output when an assert method fails
    maxDiff = None

    def test_user_class(self):
        """creats and test a new user object"""
        uo00 = User()

        self.assertEqual(uo00.__class__.__name__, "User")
        self.assertTrue(hasattr(uo00, "id"))
        self.assertEqual(uo00.created_at, uo00.updated_at)
        self.assertTrue(hasattr(uo00, "email"))
        self.assertTrue(hasattr(uo00, "password"))
        self.assertTrue(hasattr(uo00, "first_name"))
        self.assertTrue(hasattr(uo00, "last_name"))

    def test_email(self):
        """tests the public class attribute email"""
        uo01 = User()

        if hasattr(uo01, "email"):
            self.assertEqual(uo01.email, "")
            setattr(uo01, "email", "dodo@well.com")
        self.assertEqual(uo01.email, "dodo@well.com")

    def test_password(self):
        """tests the public class attribute password"""
        uo02 = User()

        if hasattr(uo02, "password"):
            self.assertEqual(uo02.password, "")
            setattr(uo02, "password", "Let_it_be_our_secret")
        self.assertEqual(uo02.password, "Let_it_be_our_secret")

    def test_first_name(self):
        """tests the public class attribute first_name"""
        uo03 = User()

        if hasattr(uo03, "first_name"):
            self.assertEqual(uo03.first_name, "")
            setattr(uo03, "first_name", "Kamaru")
        self.assertEqual(uo03.first_name, "Kamaru")

    def test_last_name(self):
        """tests the public class attribute last_name"""
        uo04 = User()

        if hasattr(uo04, "last_name"):
            self.assertEqual(uo04.last_name, "")
            setattr(uo04, "last_name", "Usman")
        self.assertEqual(uo04.last_name, "Usman")
