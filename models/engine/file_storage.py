#!/usr/bin/python3
"""Serializes instances to a JSON
file and deserializes JSON file to instances"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as fd:
            json.dump(new_dict, fd, indent="")

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file"""
        dict_ = {}

        try:
            with open(self.__file_path, "r") as fd:
                dict_ = json.load(fd)
                for key, value in dict_.items():
                    obj = eval(value["__class__"] + "(**value)")
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
