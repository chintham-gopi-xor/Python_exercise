"""Decorator pattern worked example: stackable wrappers around a data store.

Not to be confused with Python's @decorator syntax: here we wrap objects, not functions.
"""

import base64
import codecs
import zlib


class MemoryStore:
    def __init__(self):
        self.data = ""

    def write(self, text):
        self.data = text

    def read(self):
        return self.data


class StoreWrapper:
    """Base wrapper: same interface as the wrapped object, delegates everything."""

    def __init__(self, inner):
        self._inner = inner

    def write(self, text):
        self._inner.write(text)

    def read(self):
        return self._inner.read()


class Rot13Store(StoreWrapper):
    def write(self, text):
        super().write(codecs.encode(text, "rot13"))

    def read(self):
        return codecs.decode(super().read(), "rot13")


class CompressedStore(StoreWrapper):
    def write(self, text):
        packed = base64.b64encode(zlib.compress(text.encode())).decode()
        super().write(packed)

    def read(self):
        return zlib.decompress(base64.b64decode(super().read())).decode()


if __name__ == "__main__":
    raw = MemoryStore()
    secure = Rot13Store(raw)
    secure.write("Hello World")
    print(raw.read())
    print(secure.read())

    big = MemoryStore()
    stacked = CompressedStore(Rot13Store(big))
    message = "abc " * 100
    stacked.write(message)
    print(len(message), len(big.read()) < len(message))
    print(stacked.read() == message)
