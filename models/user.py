#!/usr/bin/python3

"""This module defines the User class which inherit from the
BaseModel class and is a representation of a user/sojourner
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User: is the representation of a sojourner in the airbnb
    application. It defines methods and attributes to identify
    manage and track a User Object

    Attributes:
        `email`(str): email of the user
        `password` (str): password of the user
        `first_name` (str): first name of the user
        `last_name` (str): last name of the user

    """
    email: str = ""
    pasword: str = ""
    first_name: str = ""
    last_name: str = ""
