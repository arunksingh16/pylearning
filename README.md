
## PYTHON EXAMPLES

Raw string: 

```
rawstring = r'Om\Namah:\Shivay'
print(rawstring)
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

```
LST = [1,2,3]
LST1 = []
```

DICT:

```
DCT: {'KEY1': 'VAL1', 'KEY2':'VAL2'}
DCT2 = {}
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
