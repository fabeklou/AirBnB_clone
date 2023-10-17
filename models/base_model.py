#!/usr/bin/python3

"""This module contains the BaseModel class, which is the parent
class of all the other classes
"""

from copy import deepcopy
from datetime import datetime
import uuid
from models import storage


class BaseModel:
    """This class defines a basic structure for BaseModel objects and
    his subClasses (`User`, `State`, `City`, `Place`)

    Attributes:
        `id` (str): is an identifier unique for evry BaseModel object
        `created_at` (datetime): is a datetime object representing the exact
            creation time of the BaseModel object (timestamp)
        `updated_at` (datetime): is a datetime object representing
            the last time a change was made to a BaseModel object

    """

    def __init__(self, *args, **kwargs):
        """This is the contructor of new BaseModel Objects,
        It sets the id, the creation and update time of a new object

        Args:
            *args (:tuple):
                variable number of positional arguments (is not used)
            **kwargs (:dict):
                collection of attribut/value paires, to create a new
                BaseModel object from

        """
        if not kwargs:
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            self.id = str(uuid.uuid4())
            storage.new(self)
            return
        for attr, value in kwargs.items():
            if attr == "__class__":
                continue
            if attr == "created_at" or attr == "updated_at":
                setattr(self, attr, datetime.strptime(
                    value, "%Y-%m-%dT%H:%M:%S.%f"))
                continue
            setattr(self, attr, value)

    def __str__(self):
        """This magic method returns the user readable string form of
        an object that can be understood by the end users

        Returns:
            (str): a human-readable string to be printed or to convert
                a BaseModel object into

        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """save: updates the instance attribute `updated_at`
        with the current datetime

        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """to_dict: returns a dictionary containing all keys/values of
        __dict__ of the instance

        """
        dict_attrs: dict = deepcopy(self.__dict__)
        class_name = self.__class__.__name__

        dt_created_at = getattr(self, "created_at")
        dt_updated_at = getattr(self, "updated_at")

        iso_created = dt_created_at.isoformat("T", "auto")
        iso_updated = dt_updated_at.isoformat("T", "auto")

        dict_attrs.update(__class__=class_name,
                          updated_at=iso_updated, created_at=iso_created)
        return dict_attrs
