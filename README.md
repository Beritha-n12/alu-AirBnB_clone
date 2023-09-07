# alu-AirBnB_clone
![65f4a1dd9c51265f49d0](https://github.com/Umutoniwasepie/alu-AirBnB_clone/assets/116735775/48df9495-b0d0-4eb4-9e58-378df6eb0202)
Welcome to the AirBnB clone project!


## Project Description

This is the first step in building an Airbnb clone web application. In this step, we will create a command interpreter to manage Airbnb objects. This command interpreter will be used as the foundation for the entire project, including HTML/CSS templating, database storage, API, and front-end integration.

## Learning Objectives
At the end of this project, we are expected to be able to explain:

-How to create a Python package
-How to create a command interpreter in Python using the cmd module
-What is Unit testing and how to implement it in a large project
-How to serialize and deserialize a Class
-How to write and read a JSON file
-How to manage datetime
-What is an UUID
-What is *args and how to use it
-What is **kwargs and how to use it
-How to handle named arguments in a function

## Command Interpreter
What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
-Create a new object (ex: a new User or a new Place)
-Retrieve an object from a file, a database etc…
-Do operations on objects (count, compute stats, etc…)
-Update attributes of an object
-Destroy an object

The command interpreter allows you to perform various actions on Airbnb objects, including creating, retrieving, updating, and deleting them. It also provides helpful commands like `help` and `quit`.

### How to Start

To start the command interpreter, run `./console.py` in your terminal.

### How to Use

Once the interpreter is running, you can use the following commands:

- `create`: Create a new Airbnb object.
- `show`: Retrieve information about an object.
- `update`: Update the attributes of an object.
- `destroy`: Delete an object.
- `all`: List all objects or objects of a specific class.
- `quit` or `EOF`: Exit the program.

### Execution
Your shell should work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
But also in non-interactive mode: (like the Shell project in C)

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$

### Testing
Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:

$ python3 unittest -m discover tests
Alternatively, you can specify a single test file to run at a time:

$ python3 unittest -m tests/test_console.py

## Authors

- Beritha NIYOTWAGIRA <Beritha-n12>
- Pierrette UMUTONIWASE <Umutoniwasepie>
