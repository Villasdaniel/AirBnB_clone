#!/usr/bin/python3
"""contains the entry points of the command interpreter"""

import cmd
import sys
import json
import models
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
                    dics.pop(args[0] + "." + args[1])
                    storage.save()
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
        elif(args[0] + "." + args[1] not in storage.all().keys()):
            print("** no instance found **")
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
                except ValueError:
                    try:
                        x = float(args[3].replace('"', ''))
                    except ValueError:
                        try:
                            x = str(args[3].replace('"', ''))
                        except ValueError:
                            pass
                args[3] = args[3].replace('"', '')
                d1 = {args[2]: x}
                instance.__dict__.update(d1)
            else:
                print("** no instance found **")

    def do_count(self, arg):
        """
        Count number of class instances
        """
        count = 0
        args = arg.split()
        if(args[0] not in self.returdic().keys()):
            print(" class doesn't exist ")
        else:
            list1 = []
            all_dict = storage.all()
            for key, value in all_dict.items():
                if args[0] in key:
                    count += 1
            print(count)

    def default(self, inp):
        """ Method for the advanced tasks """
        inp_split = inp.split(".")
        if inp_split[1] == "all()":
            return self.do_all(inp_split[0])
        elif inp_split[1] == "count()":
            return self.do_count(inp_split[0])
        elif "show" in inp_split[1]:
            try:
                s = str(inp_split[1])
                args = s[s.find("(")+1:s.find(")")].replace(",", " ")\
                    .replace('"', "")
                return self.do_show(str(inp_split[0]) + " " + args)
            except:
                print("Usage: <class name>.show(\"<id>\")")
        elif "destroy" in inpsplit[1]:
            try:
                id = inp_split[1].split('"')
                return self.do_destroy(str(inpsplit[0]) + " " + id[1])
            except:
                print("Usage: <class name>.destroy(\"<id>\")")
        elif "update" in inp_split[1]:

            s = str(inp_split[1])
            args = s[s.find("(")+1:s.find(")")].\
                replace(",", " ").replace('"', "")
            return self.do_update(str(inp_split[0]) + " " + args)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
