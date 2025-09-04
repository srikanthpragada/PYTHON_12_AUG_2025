import math_funs as mf
from math_funs import ispositive
from math_funs import *

import sys

# Add new folder to search path
sys.path.insert(0, r'c:\classroom\python\demo\stlib')
print(sys.path) # Module Search Path

import str_funs

print(mf.iseven(10))
print(ispositive(-10))
print(str_funs.count_upper('PYthon'))

print(dir(mf))



