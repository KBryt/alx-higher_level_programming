# 0x0C-python-almost_a_circle

## Resources
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [JSON encoder and decoder](https://docs.python.org/3/library/json.html)
- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)

## models/

### base.py
This file contains a class ``` Base ```. It is the '*base*' of all other classes in this project. Main goal is to manage ``` id ``` attribute to avoid code duplication.

### rectangle.py
Contains the rectangle class that implements the base class. 

### square.py
This file contains the a class Square that implements the class Rectangle.

###  __init__.py
This makes the folder a python module.

## tests/
This folder contains the test files and folders of this project.

### test_models/
Test folder contains unittests for the model folder.

#### test_base.py
Test case  for ```base.py```.

#### test_rectangle.py
Test case for ```rectangle.py```.

#### test_square.py
Test case for ```square.py```.
