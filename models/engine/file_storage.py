#!/usr/bin/python3

"""
Store first object
"""

import json
import os.path
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """ initializing """
        pass

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        FileStorage.__objects[key] = obj

    def reset(self):
        """reset the storage to an yempty state"""
        self.__objects = {}
        with open(self.__file_path, 'w') as file:
            file.write("{}")

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        objects_dict = {key: obj.to_dict()
                        for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objects_dict, file)

    def delete(self, obj=None):
        """ Delete object from _object """
        if obj is not None:
            key = f"{type(obj).__name__}.{obj.id}"
            if key in self.__objects:
                del self.__objects[key]
                self.save

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""

        class_list = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
        }

        try:
            with open(FileStorage.__file_path, "r") as file:
                objects_dict = json.load(file)
                for key, value in objects_dict.items():
                    class_name = value.pop("__class__", None)
                    if class_name:
                        obj_class = eval(class_name)
                        obj_instance = obj_class(**value)
                        FileStorage.__objects[key] = obj_instance
        except FileNotFoundError:
            pass
