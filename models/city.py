#!/usr/bin/python3

"""This module defines the City class which inherit from the
BaseModel class and is a representation of a City in which
a place (house/room) may be located
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City: is the data representation of a City object
    and is a state in which a place is located

    Attributes:
        `state_id` (str): identifier of the state the city
            belong to (State.id)
        `name` (str): name of the City
    """
    state_id: str = ""
    name: str = ""
