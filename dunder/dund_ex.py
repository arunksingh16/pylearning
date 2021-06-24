import math
import sys

def dosquare(x):
    y = int(x) ** 2
    return(print(y))

print(__name__)

def main(x):
    dosquare(x)

if __name__ == '__main__':
    main(sys.argv[1])



## dunder name in not equal to dunder main then the module knows that it is being imported and dunder name is equal to main then module
## knows that it has to be executed
