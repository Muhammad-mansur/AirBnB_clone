#!/usr/bin/python3

""" User model """

from models.base_model import BaseModel


class User(BaseModel):
    """ A class user that inherits from BaseModel """
    def __init__(self, *args, **kwargs):
        """ Initialize user class """
        super().__init__(args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        