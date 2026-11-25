from functools import wraps

OPERATIONS = {}


def register(name):
    
    def decorator(func):
        OPERATIONS[name] = func
        return func
    return decorator


def validate_numbers(func):
    
    @wraps(func)
    def wrapper(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError(f"{func.__name__} requires numeric arguments")
        return func(a, b)
    return wrapper


@register("add")
@validate_numbers
def add(a, b):
    return a + b


@register("sub")
@validate_numbers
def sub(a, b):
    return a - b


@register("mul")
@validate_numbers
def mul(a, b):
    return a * b


@register("div")
@validate_numbers
def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def calculate(op_name, a, b):
    try:
        func = OPERATIONS[op_name]
    except KeyError:
        raise ValueError(f"Unknown operation: {op_name}") from None
    return func(a, b)


def apply_twice(func, value):
    return func(func(value))


def compose(f, g):
    def h(x):
        return f(g(x))
    return h


if __name__ == "__main__":
    print(calculate("add", 2, 3))
    print(calculate("mul", 4, 5))
    print(apply_twice(lambda s: s + "!", "hey"))
    shout = compose(str.upper, lambda s: s + "!")
    print(shout("hello"))
    print(add.__name__, callable(add), type(add).__name__)
    print(sorted(OPERATIONS))

    try:
        calculate("pow", 2, 3)
    except ValueError as err:
        print("Error:", err)

    try:
        calculate("add", "2", 3)
    except TypeError as err:
        print("Condition Error:", err)
