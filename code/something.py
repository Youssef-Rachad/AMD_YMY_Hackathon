import os


pass =  os.getenv("Password")

print(pass)


def do_something(something):
    print(something)
    do_nothing()

def do_nothing():
    pass



do_something(pass + "AGAIN")