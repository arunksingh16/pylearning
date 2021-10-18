import sys

def print_hi(name):
    print(f'Hi, {name}')

if __name__ == '__main__':
    x = sys.argv[1]
    print_hi(x.capitalize())
