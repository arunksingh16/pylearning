# The format() method formats the specified value(s) and insert them inside the string's placeholder.

detailsHostname = "details" if (os.environ.get("DETAILS_HOSTNAME") is None) else os.environ.get("DETAILS_HOSTNAME")
port = "port" if (os.environ.get("PORTS") is None) else os.environ.get("PORTS")

details = {
    "name": "http://{0}:{1}".format(detailsHostname, port),
    "endpoint": "details",
    "children": []
}

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)

