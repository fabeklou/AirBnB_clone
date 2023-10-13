#!/usr/bin/python3

"""This module defines the Review class which inherit from the
BaseModel class and is a representation of the appreciation
given by a costumer to a place
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review: is the representation of an appreciation given
    by a guest to a place rented on the airbnb_clone app

    It is intended to help other guets that may be interested
    in that particular place to gauge if the place could be
    convient for them or not

    Attributes:
        `place_id` (str): is the identifier of the reviewed place
        `user_id` (str): is the identifier of the user that
            reviewed the place
        `text` (str): is what the user says about the place

    """
    place_id: str = ""
    user_id: str = ""
    text: str = ""
