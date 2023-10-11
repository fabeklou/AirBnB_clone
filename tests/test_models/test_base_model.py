#!/usr/bin/python3

"""This module defines a TestBaseModel class, which is used to
test the BaseModel class form the models package
"""

from contextlib import redirect_stdout
from datetime import datetime
from models.base_model import BaseModel
import io
from time import sleep
import unittest
import uuid


def capture_stdout(obj):
    """intercept the string printed to stdout
    and returns it

    Args:
        obj(:any): the object which output should be captured

    """
    captured_output = io.StringIO()

    with redirect_stdout(captured_output):
        print(obj)

    captured_string = captured_output.getvalue()
    return captured_string


class TestBaseModel(unittest.TestCase):
    """Defines test cases for BaseModel class"""

    # Show the whole output when an assert method fails
    maxDiff = None

    def test_new_object(self):
        """creates new BaseModel objects and test his attributes"""
        bm00 = BaseModel()
        sleep(1)   # Wait for 1sec
        bm01 = BaseModel()

        self.assertIsInstance(bm00, BaseModel)
        self.assertIsInstance(bm01, BaseModel)

    def test_basemodel_with_named_arg(self):
        """creates a BaseModel object from a dict"""
        uuid0 = str(uuid.uuid4())
        c_at_dt = datetime.now()
        c_at_str = c_at_dt.isoformat("T", "auto")

        bm02 = BaseModel(id=uuid0, created_at=c_at_str, updated_at=c_at_str)
        self.assertEqual(bm02.id, uuid0)
        self.assertEqual(bm02.created_at, datetime.strptime(
            c_at_str, "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(bm02.created_at, bm02.updated_at)

        bm02.save()
        self.assertLess(bm02.created_at, bm02.updated_at)

        bm02.name = "Fab the GOAT!"
        self.assertIn("name", bm02.__dict__)
        self.assertEqual(bm02.name, "Fab the GOAT!")

    def test_basemodel_with_positional_arg(self):
        """attempt to creates a BaseModel object from
        positional arguments"""
        uuid00 = str(uuid.uuid4())
        c_at0 = datetime.now()

        bm03 = BaseModel(uuid00, c_at0)

        # positional args are simply ignored
        self.assertNotEqual(bm03.id, uuid00)
        self.assertNotEqual(bm03.created_at, c_at0)
        self.assertNotEqual(bm03.updated_at, c_at0)

    def test_id_attr(self):
        """test the `id` attribute"""
        bm05 = BaseModel()
        sleep(1)   # Wait for 1sec
        bm06 = BaseModel()

        self.assertNotEqual(bm05.id, bm06.id)   # Make sure ids are unique

        self.assertIsInstance(bm05.id, str)
        self.assertIsInstance(bm06.id, str)

        bm05.id = "This is messy"
        self.assertEqual(bm05.id, "This is messy")

    def test_created_at_attr(self):
        """test the public instance attribute `created_at`"""
        bm07 = BaseModel()
        sleep(1)   # Wait for 1sec
        bm08 = BaseModel()

        self.assertIsInstance(bm07.created_at, datetime)
        self.assertIsInstance(bm08.created_at, datetime)

        self.assertNotEqual(bm07.created_at, bm08.created_at)
        self.assertEqual(bm07.created_at, bm07.updated_at)

    def test_updated_at_attr(self):
        """test the public instance attribute `updated_at`"""
        bm09 = BaseModel()
        sleep(1)   # Wait for 1sec
        bm10 = BaseModel()

        self.assertIsInstance(bm09.updated_at, datetime)
        self.assertIsInstance(bm10.updated_at, datetime)

        self.assertNotEqual(bm09.updated_at, bm10.updated_at)
        self.assertEqual(bm10.created_at, bm10.updated_at)

        bm10.updated_at = datetime.now()
        self.assertNotEqual(bm10.created_at, bm10.updated_at)

    def test__str__(self):
        """tests the `__str__` magic method"""
        bm11 = BaseModel()
        sleep(1)   # Wait for 1sec
        bm12 = BaseModel()

        self.assertEqual(bm11.__str__(), "[{}] ({}) {}".format(
            bm11.__class__.__name__, bm11.id, bm11.__dict__))
        self.assertEqual(str(bm11), "[{}] ({}) {}".format(
            bm11.__class__.__name__, bm11.id, bm11.__dict__))
        self.assertEqual(capture_stdout(bm12), "[{}] ({}) {}\n".format(
            bm12.__class__.__name__, bm12.id, bm12.__dict__))

    def test_save_(self):
        """tests the instance method `save`"""
        bm13 = BaseModel()

        self.assertEqual(bm13.updated_at, bm13.created_at)

        bm13.save()
        self.assertGreater(bm13.updated_at, bm13.created_at)

    def test_to_dict(self):
        """tests the instance method `to_dict`"""
        bm14 = BaseModel()
        bm15 = BaseModel()
        dct: dict = bm14.to_dict()

        self.assertIn("id", dct)
        self.assertIn("created_at", dct)
        self.assertIn("updated_at", dct)
        self.assertEqual(dct["__class__"], "BaseModel")

        with self.assertRaises(KeyError):
            print(dct["unknown"])

        bm15.name = "Fab the Great !"
        dct2 = bm15.to_dict()
        self.assertIn("name", dct2)
        self.assertIs(dct2["name"], "Fab the Great !")
