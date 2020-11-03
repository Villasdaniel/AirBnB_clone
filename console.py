#!/usr/bin/python3
"""contains the entry points of the command interpreter"""


import cmd
import sys
import json
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """contains the entry points of the command interpreter"""

    prompt = "(hbnb)"
    __dictio = {"BaseModel": BaseModel, "User": User, "State": State,
                "City": City, "Amenity": Amenity,
                "Place": Place, "Review": Review}

    def returdic(self):
        """return dictionary with all classes"""
        return self.__dictio

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF"""
        return True

    def emptyline(self):
        """empty line + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):
        """create a new instance"""
        if len(arg) == 0:
            print("** class name missing **")
            return
        elif arg not in self.returdic().keys():
            print("** class doesn't exist **")
        else:
            instance = self.returdic()[arg]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """Show a specific instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.returdic().keys():
            print("** class doesn't exist **")
        elif (len(args) == 1) and (args[0] in self.returdic().keys()):
            print("** instance id missing **")
        else:
            dics = storage.all()
            if dics:
                ids = dics.get(str(args[0]) + "." + str(args[1]))
                if ids:
                    print(ids)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Destroy a specific instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.returdic().keys():
            print("** class doesn't exist **")
        elif (len(args) == 1) and (args[0] in self.returdic().keys()):
            print("** instance id missing **")
        else:
            dics = storage.all()
            if dics:
                ids = dics.get(str(args[0]) + "." + str(args[1]))
                if ids:
                    del dics[str(args[0]) + "." + str(args[1])]
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """Show all instancess"""
        lists = []
        args = arg.split()
        dics = storage.all()
        if arg:
            if args[0] not in self.returdic().keys():
                print("** class doesn't exist **")
                return
            else:
                for key, value in dics.items():
                    clase = key.split(".")
                    if args[0] == clase[0]:
                        lists.append(str(value))
                print(lists)
                return
        if dics:
            for key, value in dics.items():
                lists.append(str(value))
        print(lists)

    def do_update(self, arg):
        """update a existing instance or create a new one"""
        args = arg.split()
        if len(arg) < 1:
            print("** class name missing **")
        elif(args[0] not in self.returdic().keys()):
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            all_dict = storage.all()
            instance = all_dict.get(str(args[0]) + "." + str(args[1]))
            if instance:
                try:
                    x = int(args[3].replace('"', ''))
                except:
                    try:
                        x = float(args[3].replace('"', ''))
                    except:
                        try:
                            x = str(args[3].replace('"', ''))
                        except:
                                    pass
                args[3] = args[3].replace('"', '')
                d1 = {args[2]: x}
                instance.__dict__.update(d1)
            else:
                print("** no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
