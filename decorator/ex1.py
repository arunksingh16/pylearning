import datetime

def log(val1):
    def wrapper(*args, **kwargs):
        with open("./logs.txt", "a") as f:
            f.write("Called function with " + " ".join([str(arg) for arg in args]) + " at " + str(datetime.datetime.now()) + "\n")  
        v = val1(*args, **kwargs)
        return v
    return wrapper

@log
def run(a, b, c=10):
    print(a+b+c)

run(1,3,c=10)
