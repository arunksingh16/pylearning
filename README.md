## Python Tips

Use PEP8 code style guide for Python
```
pip install pep8
python -m pep8 <py file>

```

`dir(object)` returns a list of attributesthat are accessible via the object
`globals()` returns a dictionary of the attributescurrently in the global namespace, along with their values.
`locals()` returns a dictionary of the attributes inthe current local namespace (e.g., within a function),along with their values.

### Python Version details at runtime 

```
import sys
print(sys.version_info)
print(sys.version)
```

### pipenv
Pipenv is a tool that provides all necessary means to create a virtual environment for your Python project. Pipenv also generates the Pipfile.lock file, which is used to produce deterministic builds and create a snapshot of your working environment. It also introduces two new files, the Pipfile (which is meant to replace requirements.txt) and the Pipfile.lock (which enables deterministic builds).

`Pipenv uses pip and virtualenv under the hood but simplifies their usage with a single command line interface.`

using pipenv
```
pip install --user pipenv
python3.7 -m pipenv --python path\to\python
python3.7 -m pipenv install --dev
```
### setup.py
https://github.com/navdeep-G/setup.py


### PIP UPDATES

```
pip list --outdated

pip install <package_name> --upgrade

# FOR SPECIFIC USER
pip install <package_name> --upgrade --user

```
### Note

- All functions return a value, if you dont specify then it is none. functions are first-class objects.
- Mutable
- Any directory with an __init__.py file is considered a Python package. A file modu.py in the directory pack/ is imported with thestatement import pack.modu.
 


### PYTHON EXAMPLES

`Everything is an object in Python`

type:
dir: 

```
>>> import math

>>> type(math)
<class 'module'>

# tells about module attributes
>>> dir(math)


>>> type(math.cos)
<class 'builtin_function_or_method'>

>>> dir(math.cos)

['__call__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__self__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__text_signature__']

>>> math.cos.__doc__
'Return the cosine of x (measured in radians).'
>>>


```


Raw string: 

```
rawstring = r'Om\Namah:\Shivay'
print(rawstring)
```

Partition

```
>>> x,y,z = "Lon:Del".partition(':')
>>> x
'Lon'
>>> y
':'
>>> z
'Del'
>>>

```


range:

```
range(stop)
range(start, stop)
range(start, stop, step)


```




while loop:

```
while c !=0:
    print(c)
    c -= 1

while True:
    response = input()
    if int(response) == 1:
        break
```

if loop:

```
if c == 111:
    print("OK")
else:
    if c == 110:
        print("SECOND OK")
    else:
        print("SECOND not OK")

```

FOR loop:

```
x = ["shiv", "hanu"]
for i in x:
    print(i)
```


methods

```
print("Enter your Name: ") 
res = input()
print("Your name is : " + res.capitalize())
```

Bytes:

```
>>> d = b'this is bytes'
>>> d.split()
[b'this', b'is', b'bytes']
>>> d[0]
116

>>> ak = "Hi this is utf8"
>>> data = ak.encode('utf8')
>>> print(data)
b'Hi this is utf8'
>>> 
>>> ak = data.decode('utf8')
>>> print(ak)
Hi this is utf8
```

LIST:
- 

```
LST = [1,2,3]
LST1 = []
# slicing
LST[1:3]
LST[1:]

>> LST = ["ARUN", "SAM", "TIPPU"]
>> LST.index('ARUN')
0
>> "ARUN" in LST
True
```

DICT:
- keys are immutable
- values may be immutable
```
DCT: {'KEY1': 'VAL1', 'KEY2':'VAL2'}
DCT2 = {}
```

TUPLE: 

```
>>> t = ("val",1)
>>> type(t)
<class 'tuple'>

```

Importing a function:

1. file with a function
```
import function_example

function_example.method1()

```
2. calling directly a function

```
from function_example import *
method1()

```

function with default argument: Arg with default values must come after those without default values

```
import time
def createbanner(msg, border="-"):
    l = border * len(msg)
    print(l)
    print(msg)
    print(l) 

createbanner("This is Banner")
createbanner(time.ctime(), "$")

```

enumerate:

constructs an iterable of (index, value) tuple around another iterable object

```
>>> t = [7, 8, 6]

>>> for i in enumerate(t):
...     print(i)
...
(0, 7)
(1, 8)
(2, 6)
>>>

```
ex 2 

```
a = ["icky", "icky", "icky", "p-tang"]
for i, item in enumerate(a):
    print("{i}: {item}".format(i=i, item=item))
```


Very bad
```
from modu import *
[...]
x = sqrt(4)  # Is sqrt part of modu? A builtin? Defined above?
````
Better
```
from modu import sqrt
[...]
x = sqrt(4)  # sqrt may be part of modu, if not redefined in between
```
Best
```
import modu
[...]
x = modu.sqrt(4)  # sqrt is visibly part of modu's namespace
```


### decorators
Python decorators are mechanism to change or modify the behaviour of function or methods without changing any of its code. 

```
# following example will tell you how long a function takes to run
import time

def func_f1(val1):
    def wrapper():
        a = time.time()
        val1()
        print("function took:", time.time() - a, "seconds")
    return wrapper

def run():
    time.sleep(2)

# without decorator
func_f1(run)()

@func_f1
def quick():
    time.sleep(2)

# with decorator
quick()

```

### Exceptions

```
try:
 # runs first
except:
 # runs when exception occur in try block
else:
 # execute when try block is a success
finally:
 # always execute
```

### Set Algebra
Python set can support powerful algebra options
```
# sets are define
A = {0, 2, 4, 6, 8};
B = {1, 2, 3, 4, 5};
  
# union
print("Union :", A | B)
  
# intersection
print("Intersection :", A & B)
  
# difference
print("Difference :", A - B)
  
# symmetric difference
print("Symmetric difference :", A ^ B)
```
### Python protocols 
Python Built in collection can be organised in protocols
```
Protocol

Implementing collections

Container

str, list, dict, range, tuple, set, bytes

Sized

str, list, dict, range, tuple, set, bytes

Iterable

str, list, dict, range, tuple, set, bytes

Sequence

str, list, tuple, range, bytes

Mutable Sequence

list

Mutable Set

set

Mutable Mapping

dict
```

Note: 

- Everything including Functions and classes are in Python is an object.
- Decorators work with classes, methods as well
- Every object is an instance of a class.


### good projects for ref:
https://github.com/postmanlabs/httpbin

