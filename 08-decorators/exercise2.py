def announce(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper


def shout(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper


@announce
def add(a, b):
    return a + b


@shout
def greet(name, punctuation="!"):
    return f"hello {name}{punctuation}"


if __name__ == "__main__":
    print(add(2, 3))
    print(greet("ana"))
    print(greet("ben", punctuation="?"))

    def sub(a, b):
        return a - b

   
    sub = announce(sub)
    print(sub(10, 4))
    print(add.__name__)
