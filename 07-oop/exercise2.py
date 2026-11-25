import math


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, (int, float)) and not isinstance(other, bool):
            return Vector2D(self.x * other, self.y * other)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __iter__(self):
        yield self.x
        yield self.y


a = Vector2D(3, 4)
b = Vector2D(1, 2)
print(repr(a))
print(a)
print(a + b)
print(a - b)
print(a * 2)
print(2 * a)
print(abs(a))
print(a == Vector2D(3, 4))
print(a == b)
print(bool(Vector2D(0, 0)))
x, y = a
print(x, y)
try:
    a + 5
except TypeError as err:
    print("TypeError:", err)
