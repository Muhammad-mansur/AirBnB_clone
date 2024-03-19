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
        if 'id' not in kwargs:
            self.id = str(uuid.uuid4())
        else:
            self.id = kwargs['id']
        if 'created_at' not in kwargs:
            self.created_at = datetime.datetime.now()
        else:
            self.created_at = datetime.datetime.strptime(kwargs['created_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
        if 'udated_at' not in kwargs:
            self.updated_at = datetime.datetime.now()
        else:
            self.updated_at = datetime.datetime.strptime(kwargs['updated_at'],
                    '%Y-%m-%dT%H:%M:%S.%f')
            models.storage.new(self)

    def __str__(self):
        """ string representation """
        created_at_str = self.created_at.isoformat() \
                if isinstance(self.created_at, datetime.datetime) else self.created_at
        updated_at_str = self.updated_at.isoformat() \
                if isinstance(self.updated_at, datetime.datetime) else self.updated_at
        output_dict = {
                'id': self.id,
                'created_at' : created_at_str,
                'updated_at' : updated_at_str,
                '__class__' : self.__class__.__name__
                }
        formatted_output = f"{self.__class__.__name__}.{self.id} {output_dict}"
        return formatted_output

    def save(self):
        """
        updates the public instance attribute 'updated_at'
        with the current datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
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
