"""
This file defines the public API your package exposes.

The reasoning behind this is it allows you to "import os" in mypackage.py
and then when users "import mypackage" they won't be bothered by "os"
appearing in "dir(mypackage)".

If you don't want to explicitly expose everything you can use:
"from mypackage import *"

"""

VERSION = '1.0'

from mypackage import a_function_of_mine
from mypackage import MyClass
