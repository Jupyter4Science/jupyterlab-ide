import os
import sys

import sys, os

from subprocess import Popen, PIPE


import mypkg.sibling
from mypkg import sibling
from mypkg.sibling import example

import myclass
import foo.bar.yourclass



from . import sibling
from .sibling import example

from myclass import MyClass
from foo.bar.yourclass import YourClass