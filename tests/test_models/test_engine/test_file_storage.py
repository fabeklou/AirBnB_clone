#!/usr/bin/python3

"""This module tests the file_storage module
from the engine package
"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import unittest


class TestFileStorage(unittest.TestCase):
    """Defines test cases for the FileStorage class"""

    # Show the whole output when an assert method fails
    maxDiff = None

    def test_new_filestorage_obj(self):
        """creates and tests a new file_storage object"""
        fso00 = FileStorage()
        bmo00 = BaseModel()

    def test__file_path(self):
        """tests the __file_path private class attribute"""
        fso01 = FileStorage()
        bmo01 = BaseModel()

        # self.assertTrue("__file_path" in fso01.__dict__)

    def test__objects(self):
        """tests the __objects private class attribute"""
        fso02 = FileStorage()
        bmo02 = BaseModel()

        # self.assertTrue("__objects" in fso02.__dict__)

    def test_all_method(self):
        """tests the instance method all"""
        fso03 = FileStorage()
        bmo03 = BaseModel()

    def test_save_method(self):
        """tests the instance method save"""
        fso04 = FileStorage()
        bmo04 = BaseModel()

    def test_reload_method(self):
        """tests the instance method reload"""
        fso05 = FileStorage()
        bmo05 = BaseModel()

    def test_with_new_basemodel_obj(self):
        """tests"""
        fso06 = FileStorage()
        bmo06 = BaseModel()

    def test_when_basemodel_obj_saved(self):
        """tests"""
        fso07 = FileStorage()
        bmo07 = BaseModel()
