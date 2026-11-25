"""Singleton worked example: one shared log manager for the whole application."""


class LogManager:
    _instance = None

    def __new__(cls):
        # __new__ runs before __init__, so we decide here whether to build a new object
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.records = []
        return cls._instance

    def log(self, level, message):
        self.records.append(f"[{level}] {message}")


# The most Pythonic singleton is often just a module-level object:
# create `logs = LogManager()` once in a module and import it everywhere.


if __name__ == "__main__":
    a = LogManager()
    b = LogManager()
    print(a is b)
    a.log("INFO", "service started")
    b.log("ERROR", "disk almost full")
    print(b.records)
    print(len(a.records))
