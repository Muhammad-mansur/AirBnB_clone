#!/usr/bin/python3

"""
Store first object
"""

import os
import json


class FileStorage:
    """
    Serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}
    
    def __init__(self):
        pass
    
    def all(self):
        """ returns the dictionary __objects """
        return self.__objects
    
    def new(self, obj):
        """ sets in __objects the obj with key """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj
        
    def save(self):
        """ serializes __objects to the JSON file """
        with open(self.__file_path, "w") as json_file:
            json.dump(self.__objects, json_file)
            
    def reload(self):
        """ deserializes the JSON file to __objects """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as json_file:
                self.__objects = json.load(json_file)
            
        else:
            """ do nothing if it doesn't exist """
            pass