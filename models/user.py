#!/usr/bin/python3

""" User Model """

from models.base_model import BaseModel


class User(BaseModel):
    """ A class user that inherits from BaseModel """
    email = ""
    password = ""
    first_name = ""
    last_name = ""