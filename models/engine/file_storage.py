#!/usr/bin/python3

"""This module defines a FileStorage class that handle
JSON string serialization and deserialization
"""

import copy
from datetime import datetime
import json


class FileStorage:
    """FilStorage: serializes instances to a JSON file and
    deserializes JSON file to instances

    """
    __file_path = "models/engine/_file-storage.json"
    """str: the path to the JSON file"""

    __objects = {}
    """dict: empty by default, will store all objects"""

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """new: adds a new objects to the __objects dict

        Args:
            obj: a direct BaseModel instance or by inheritance

        """
        key: str = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects.update({key: obj})

    def save(self):
        """save: serializes the __objects dict to the JSON file"""
        with open(self.__file_path, "w", encoding='utf-8') as fo:
            objs_copy: dict = copy.deepcopy(self.__objects)
            dicts: dict = {key: value.to_dict()
                           for key, value in objs_copy.items()}
            json.dump(dicts, fo, indent=4)

    def reload(self):
        """reload: deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        try:
            with open(self.__file_path) as fo:
                try:
                    dicts: dict = json.load(fo)
                except json.decoder.JSONDecodeError:
                    return

                funcs_dict: dict = {"BaseModel": BaseModel, "User": User,
                                    "State": State, "City": City,
                                    "Amenity": Amenity, "Place": Place,
                                    "Review": Review}

                for key, value in dicts.items():
                    class_name = value["__class__"]
                    if class_name in funcs_dict:
                        self.new(funcs_dict[class_name](**value))

        except (IOError, FileNotFoundError) as ex:
            return
