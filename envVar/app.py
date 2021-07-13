import os


def _env_var(ENVVARNAME):
    try:
        user = os.environ[ENVVARNAME]
        return(user)
    except KeyError as e:
        print("Environment variable not set")
        raise(e)

print(_env_var('PATH'))