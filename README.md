![alt text](https://camo.githubusercontent.com/4ef5f395992f891f084360fe9ee0d6846bff9fbd/68747470733a2f2f692e696d6775722e636f6d2f4e6c38764e32472e6a7067)


# AirBnB clone - The console
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

## Instanced clasess

* [BaseModel](https://github.com/Villasdaniel/AirBnB_clone/blob/main/models/base_model.py)
* [User](https://github.com/Villasdaniel/AirBnB_clone/blob/main/models/user.py)
* [State](https://github.com/Villasdaniel/AirBnB_clone/blob/main/models/state.py)
* [Review](https://github.com/Villasdaniel/AirBnB_clone/blob/main/models/review.py)
* [Place](https://github.com/Villasdaniel/AirBnB_clone/blob/main/models/place.py)
* [City](https://github.com/Villasdaniel/AirBnB_clone/blob/main/models/city.py)
* [Amenity](https://github.com/Villasdaniel/AirBnB_clone/blob/main/models/amenity.py)

## Requirements

### Python Scrips
* Allowed editors: vi, vim, emacs
* Files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* Files should end with a new line
* The first line of all files should be exactly #!/usr/bin/python3
* A README.md file, at the root of the folder of the project, is mandatory
* Code should use the PEP 8 style (version 1.7 or more)
* Files must be executable
* The length of the files will be tested using wc
* All modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests
* Allowed editors: vi, vim, emacs
* All files should end with a new line
* All test files should be inside a folder tests
* Use the unittest module
* All test files should be python files (extension: .py)
* All test files and folders should start by test_
* File organization in the tests folder should be the same as your project
* e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
* e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
* All tests should be executed by using this command: python3 -m unittest discover tests
* Test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
* All modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
* All functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
* Work together on test cases

## Examples

$ ./console.py

(hbnb) help


Documented commands (type help <topic>):
========================================
EOF  help  quit


(hbnb) 

(hbnb) 

(hbnb) all MyModel

** class doesn't exist **

(hbnb) show BaseModel

** instance id missing **

(hbnb) show BaseModel Holberton

** no instance found **

(hbnb) create BaseModel

49faff9a-6318-451f-87b6-910505c55907

(hbnb) all BaseModel

["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': 

'49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]

(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907

[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': 

'49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}

(hbnb) destroy

** class name missing **

(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"

(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907

[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 

'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}

(hbnb) create BaseModel

2dd6ef5c-467c-4f82-9521-a772ea7d84e9

(hbnb) all BaseModel

["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime

(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}", "[BaseModel] 

(49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.

datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}"]

(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907

(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907

** no instance found **

(hbnb) quit

$

## Authors

* [Daniel Villa Saldarriga](https://github.com/Villasdaniel)
* [Eliana Gomez Suarez](https://github.com/ElianaGomez2020)
