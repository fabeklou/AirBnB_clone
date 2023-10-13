#!/usr/bin/python3

"""This module defines the Amenity class which inherit from the
BaseModel class and is a representation of an amenity
a place (house/room) may have
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity: is the data representation of an Amenity object
    and is an amenity a place may have

    Attributes:
        `name` (str): name of the amenity
    """
    name: str = ""
