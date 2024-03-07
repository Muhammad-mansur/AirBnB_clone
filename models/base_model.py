#!/usr/bin/python3

""" Base Class """

import datetime
import models
import uuid


class BaseModel:
    """
    Defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        initialising
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.datetime.strptime(value,
                                                           '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:            
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
        
    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
        
    def save(self):
        """
        updates the public instance attribute 'updated_at'
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()
        
    def to_dict(self):
        """
        Returns a dictionary containing all keys/values 
        of __dict__ of the instance
        
        Creates a dictionary representation of the object
        
        Add the class name to the dictionary
        
        convert to string object in ISO format
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
