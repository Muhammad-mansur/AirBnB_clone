#!/usr/bin/python3

""" Creating a unique file storage """

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()