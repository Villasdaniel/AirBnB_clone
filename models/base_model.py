#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""


import uuid
from datetime import datetime
import models


class BaseModel:
    """defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """atributes initialization"""
        if kwargs:
            if "created_at" in kwargs and type(kwargs["created_at"] is str):
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], '%Y-%m-%dT%H:%M:%S.%f')
            if "updated_at" in kwargs and type(kwargs["updated_at"] is str):
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs.pop("__class__")
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """print name, id, dict"""
        return ("[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__))

    def save(self):
        """updates public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        d["created_at"] = self.created_at.isoformat()
        d["updated_at"] = self.updated_at.isoformat()
        return d
