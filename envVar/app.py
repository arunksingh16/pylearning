import os

try:
    user = os.environ['U1SER']
    print(user)
except KeyError as e:
    print("Environment variable not set")
    raise(e)
