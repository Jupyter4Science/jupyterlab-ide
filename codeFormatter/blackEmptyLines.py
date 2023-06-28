# in:

def foo():

    print("All the newlines above me should be deleted!")


if condition:

    print("No newline above me!")

    print("There is a newline above me, and that's OK!")


class Point:

    x: int
    y: int

# out:

def foo():
    print("All the newlines above me should be deleted!")


if condition:
    print("No newline above me!")

    print("There is a newline above me, and that's OK!")


class Point:
    x: int
    y: int