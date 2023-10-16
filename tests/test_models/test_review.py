#!/usr/bin/python3

"""This module defines a TestReview class, which is used to
test the User class form the models package
"""

from models.review import Review
import unittest


class TestReview(unittest.TestCase):
    """Defines test cases for Review class"""

    # Show the whole output when an assert method fails
    maxDiff = None

    def test_review_class(self):
        """creats and test a new Review object"""
        ro00 = Review()

        self.assertEqual(ro00.__class__.__name__, "Review")
        self.assertTrue(hasattr(ro00, "id"))
        self.assertEqual(ro00.created_at, ro00.updated_at)
        self.assertTrue(hasattr(ro00, "place_id"))
        self.assertTrue(hasattr(ro00, "user_id"))
        self.assertTrue(hasattr(ro00, "text"))

    def test_place_id(self):
        """tests the public class attribute place_id"""
        ro01 = Review()

        if hasattr(ro01, "place_id"):
            self.assertEqual(ro01.place_id, "")
            setattr(ro01, "place_id", "a0eaded2-8285-4c6c-9d05-9fb155a494c0")
        self.assertEqual(ro01.place_id, "a0eaded2-8285-4c6c-9d05-9fb155a494c0")

    def test_user_id(self):
        """tests the public class attribute user_id"""
        ro02 = Review()

        if hasattr(ro02, "user_id"):
            self.assertEqual(ro02.user_id, "")
            setattr(ro02, "user_id", "e790a4a1-bd05-46e5-ac30-4b8f18a5c96e")
        self.assertEqual(ro02.user_id, "e790a4a1-bd05-46e5-ac30-4b8f18a5c96e")

    def test_text(self):
        """tests the public class attribute text"""
        ro03 = Review()

        if hasattr(ro03, "text"):
            self.assertEqual(ro03.text, "")
            setattr(ro03, "text", "The place is great.")
        self.assertEqual(ro03.text, "The place is great.")
