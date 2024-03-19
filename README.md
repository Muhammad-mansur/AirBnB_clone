# AirBnB Clone Project

Welcome to the AirBnB clone project! This is the initial step towards building a full web application resembling AirBnB. This phase involves creating a command interpreter to manage AirBnB objects.

## Objective
The goal of this project is to:

- Implement a command-line interface to handle AirBnB objects such as User, State, City, Place, etc.
- Set up a parent class (BaseModel) responsible for initialization, serialization, and deserialization of future instances.
- Establish a serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> file.
- Create classes for AirBnB objects inheriting from BaseModel.
- Develop the first abstracted storage engine for the project: File storage.
- Construct comprehensive unit tests to validate classes and the storage engine.

## Installation
Clone this repo in your terminal:

```bash
$ git clone https://github.com/Muhammad-mansur/AirBnB_clone

## Execution
The Shell works in both interactive and non-interactive modes. Examples include:

Interactive Mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

Non-Interactive Mode:

```bash
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

## Supported Commands

The console.py command interpreter supports the following commands:

1. `help`: Display help

```bash
$ help