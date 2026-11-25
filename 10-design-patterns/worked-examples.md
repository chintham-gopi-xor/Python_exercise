# Topic 10: Design Patterns in Python - Worked Examples

Each section below explains one pattern and shows a small, runnable program. All programs live in the `examples/`
folder and were run to produce the output shown. Read the code, run it, change it, and then try the matching
exercise in `exercises.md`.

A note for beginners: do not use patterns everywhere. A pattern is a tool for a problem you actually have. If the
plain solution is already simple, keep it simple.

---

## 1. Singleton

**In one sentence:** Guarantee that a class has exactly one instance and give everyone access to it.

**Use it when:**

- Something is genuinely shared and must be consistent: configuration, a logging manager, a connection pool.
- Creating a second copy would cause bugs (two loggers writing to the same file in different formats).

**Be careful:**

- Singletons are global state in disguise; they make code harder to test. Prefer passing the object in as an argument.
- In Python a module is already a singleton: create the object once at module level and import it. Reach for `__new__` or a decorator only when you need the class form.

**Python-flavoured implementation:** override `__new__` (as shown), use a class decorator, or simply use a module-level instance.

Runnable demo: `examples/p01_singleton.py` (run it with `python examples/p01_singleton.py`).

```python
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
```

Output:

```text
True
['[INFO] service started', '[ERROR] disk almost full']
2
```

Now try it yourself: **T10-E01** in `exercises.md`.

---

## 2. Factory

**In one sentence:** Create objects through a function or method so callers do not need to know the concrete classes.

**Use it when:**

- The class to create depends on input (a string from a config file, a form field, a command-line option).
- You want to add new variants without changing the calling code.

**Be careful:**

- If there is only one class, a factory adds nothing.
- A dictionary mapping names to classes (a registry) is usually simpler in Python than a chain of if/elif.

**Python-flavoured implementation:** a dictionary of name to class (or to any callable) plus one `create_...` function; classes are first-class objects so you can store them directly.

Runnable demo: `examples/p02_factory.py` (run it with `python examples/p02_factory.py`).

```python
"""Factory worked example: create payment methods by name."""


class CreditCard:
    def __init__(self, number):
        self.number = number

    def pay(self, amount):
        return f"Charged {amount:.2f} to card ending {self.number[-4:]}"


class PayPal:
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        return f"Charged {amount:.2f} to PayPal account {self.email}"


class BankTransfer:
    def __init__(self, iban):
        self.iban = iban

    def pay(self, amount):
        return f"Requested transfer of {amount:.2f} from {self.iban}"


PAYMENT_METHODS = {
    "card": CreditCard,
    "paypal": PayPal,
    "bank": BankTransfer,
}


def create_payment_method(kind, *args, **kwargs):
    """The factory: callers never import or name the concrete classes."""
    try:
        cls = PAYMENT_METHODS[kind]
    except KeyError:
        raise ValueError(f"Unknown payment method: {kind}") from None
    return cls(*args, **kwargs)


if __name__ == "__main__":
    checkout = [
        ("card", ("4111111111111111",)),
        ("paypal", ("ana@example.com",)),
        ("bank", ("DE89370400440532013000",)),
    ]
    for kind, args in checkout:
        print(create_payment_method(kind, *args).pay(49.9))
    try:
        create_payment_method("crypto")
    except ValueError as err:
        print("Error:", err)
```

Output:

```text
Charged 49.90 to card ending 1111
Charged 49.90 to PayPal account ana@example.com
Requested transfer of 49.90 from DE89370400440532013000
Error: Unknown payment method: crypto
```

Now try it yourself: **T10-E02** in `exercises.md`.

---

## 3. Strategy

**In one sentence:** Define a family of interchangeable algorithms and choose one at run time.

**Use it when:**

- You have several ways of doing one job: sorting, pricing, shipping costs, export formats, validation rules.
- You want to replace a long if/elif on a 'mode' flag.

**Be careful:**

- Do not build a class hierarchy when a function will do; in Python any callable can be a strategy.

**Python-flavoured implementation:** pass a function (or a callable object) to the class that needs it, or keep functions in a dictionary and look them up by name.

Runnable demo: `examples/p03_strategy.py` (run it with `python examples/p03_strategy.py`).

```python
"""Strategy worked example: interchangeable shipping cost rules."""


def standard(weight_kg):
    return 4.0 + 0.5 * weight_kg


def express(weight_kg):
    return 12.0 + 1.2 * weight_kg


def free_over(threshold, fallback):
    """Build a strategy that is free above a threshold weight."""

    def strategy(weight_kg):
        return 0.0 if weight_kg >= threshold else fallback(weight_kg)

    return strategy


class Shipment:
    def __init__(self, weight_kg, strategy=standard):
        self.weight_kg = weight_kg
        self.strategy = strategy

    def cost(self):
        return round(self.strategy(self.weight_kg), 2)


if __name__ == "__main__":
    parcel = Shipment(3)
    print(parcel.cost())
    parcel.strategy = express
    print(parcel.cost())
    heavy = Shipment(20, free_over(15, standard))
    print(heavy.cost())
    light = Shipment(2, free_over(15, standard))
    print(light.cost())
    # In Python a strategy can be any callable, so plain functions are enough
    print({fn.__name__: Shipment(10, fn).cost() for fn in (standard, express)})
```

Output:

```text
5.5
15.6
0.0
5.0
{'standard': 9.0, 'express': 24.0}
```

Now try it yourself: **T10-E03** in `exercises.md`.

---

## 4. Builder

**In one sentence:** Construct a complex object step by step and validate it at the end.

**Use it when:**

- The object has many optional parts (an email with cc, attachments and a subject, a logger with several handlers).
- A constructor with ten parameters would be hard to read and easy to call wrongly.

**Be careful:**

- For objects with only a few fields, keyword arguments or a dataclass are simpler.
- Remember to return `self` from every step method, otherwise chaining breaks.

**Python-flavoured implementation:** a class with chainable methods that each return `self` and a final `build()` that validates and returns the product (often a frozen dataclass). Keyword arguments and default values cover many simple cases.

Runnable demo: `examples/p04_builder.py` (run it with `python examples/p04_builder.py`).

```python
"""Builder worked example: build an email message step by step."""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class EmailMessage:
    to: tuple
    subject: str
    body: str
    cc: tuple = ()
    attachments: tuple = field(default_factory=tuple)


class EmailBuilder:
    def __init__(self):
        self._to = []
        self._cc = []
        self._subject = ""
        self._body = ""
        self._attachments = []

    # Each step returns self so calls can be chained (a "fluent" interface)
    def to(self, address):
        self._to.append(address)
        return self

    def cc(self, address):
        self._cc.append(address)
        return self

    def subject(self, text):
        self._subject = text
        return self

    def body(self, text):
        self._body = text
        return self

    def attach(self, filename):
        self._attachments.append(filename)
        return self

    def build(self):
        if not self._to:
            raise ValueError("an email needs at least one recipient")
        if not self._subject:
            raise ValueError("an email needs a subject")
        return EmailMessage(
            tuple(self._to), self._subject, self._body,
            tuple(self._cc), tuple(self._attachments),
        )


if __name__ == "__main__":
    mail = (
        EmailBuilder()
        .to("ana@example.com")
        .to("ben@example.com")
        .cc("boss@example.com")
        .subject("Quarterly report")
        .body("Please find the report attached.")
        .attach("q3.pdf")
        .build()
    )
    print(mail)
    try:
        EmailBuilder().subject("No recipient").build()
    except ValueError as err:
        print("Error:", err)
```

Output:

```text
EmailMessage(to=('ana@example.com', 'ben@example.com'), subject='Quarterly report', body='Please find the report attached.', cc=('boss@example.com',), attachments=('q3.pdf',))
Error: an email needs at least one recipient
```

Now try it yourself: **T10-E04** in `exercises.md`.

---

## 5. Adapter

**In one sentence:** Wrap an object with an incompatible interface so that it looks like the interface your code expects.

**Use it when:**

- You use a third-party or legacy class you cannot change.
- Several providers do the same job with different method names and data formats (payment gateways, storage services).

**Be careful:**

- Do not leak the adaptee's details through the adapter; callers should see only the target interface.

**Python-flavoured implementation:** a small class that holds the adaptee and implements the target methods by translating arguments and results; duck typing means the target interface may be just a convention.

Runnable demo: `examples/p05_adapter.py` (run it with `python examples/p05_adapter.py`).

```python
"""Adapter worked example: make a Fahrenheit sensor fit a Celsius interface."""


class LegacySensor:
    """Third-party code that we cannot change."""

    def read_fahrenheit(self):
        return 98.6


class CelsiusSensorAdapter:
    """Our application expects objects with read_celsius()."""

    def __init__(self, legacy_sensor):
        self._sensor = legacy_sensor

    def read_celsius(self):
        return round((self._sensor.read_fahrenheit() - 32) * 5 / 9, 1)


def report(sensor):
    return f"Temperature: {sensor.read_celsius()} C"


if __name__ == "__main__":
    print(report(CelsiusSensorAdapter(LegacySensor())))
```

Output:

```text
Temperature: 37.0 C
```

Now try it yourself: **T10-E05** in `exercises.md`.

---

## 6. Template Method

**In one sentence:** Define the skeleton of an algorithm in a base class and let subclasses fill in individual steps.

**Use it when:**

- Several jobs follow the same sequence of steps but differ in details (importers, report generators, test setup).
- You want to guarantee the order of steps while allowing customisation.

**Be careful:**

- Inheritance couples subclasses to the base class; if the variations are small, passing functions (Strategy) may be lighter.
- Keep the template method itself non-overridable by convention and document the hooks.

**Python-flavoured implementation:** a base class with a concrete method that calls abstract methods (must be implemented) and hook methods (optional, with defaults); use `abc.ABC` to enforce the abstract steps.

Runnable demo: `examples/p06_template_method.py` (run it with `python examples/p06_template_method.py`).

```python
"""Template Method worked example: a data import pipeline with a fixed skeleton."""

import csv
import io
import json
from abc import ABC, abstractmethod


class DataImporter(ABC):
    def run(self, raw_text):
        """The template: the order of steps is fixed, the steps are customisable."""
        records = self.parse(raw_text)
        records = [r for r in records if self.is_valid(r)]
        return self.summarise(records)

    @abstractmethod
    def parse(self, raw_text):
        """Turn raw text into a list of dictionaries."""

    def is_valid(self, record):
        # Optional hook with a sensible default
        return True

    def summarise(self, records):
        return f"{len(records)} records imported"


class CsvImporter(DataImporter):
    def parse(self, raw_text):
        return list(csv.DictReader(io.StringIO(raw_text)))


class JsonImporter(DataImporter):
    def parse(self, raw_text):
        return json.loads(raw_text)

    def is_valid(self, record):
        return "id" in record


if __name__ == "__main__":
    csv_text = "id,name\n1,Ana\n2,Ben\n"
    json_text = '[{"id": 1}, {"name": "no id"}, {"id": 3}]'
    print(CsvImporter().run(csv_text))
    print(JsonImporter().run(json_text))
```

Output:

```text
2 records imported
2 records imported
```

Now try it yourself: **T10-E06** in `exercises.md`.

---

## 7. Observer

**In one sentence:** Let objects subscribe to events and be notified automatically when something happens.

**Use it when:**

- One change must trigger several independent reactions (send an email, write an audit log, update a dashboard).
- The publisher should not know who is listening.

**Be careful:**

- Unsubscribed or forgotten listeners cause surprises and memory leaks; always provide `unsubscribe`.
- One failing observer should not stop the others; decide how errors are handled.

**Python-flavoured implementation:** keep a list of callables; any function or object with `__call__` can be an observer. Libraries often call this an event bus, signals or callbacks.

Runnable demo: `examples/p07_observer.py` (run it with `python examples/p07_observer.py`).

```python
"""Observer worked example: a stock ticker that notifies subscribers of price changes."""


class StockTicker:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self._price = price
        self._observers = []

    def subscribe(self, callback):
        self._observers.append(callback)

    def unsubscribe(self, callback):
        self._observers.remove(callback)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        old, self._price = self._price, new_price
        for notify in list(self._observers):
            notify(self.symbol, old, new_price)


def print_change(symbol, old, new):
    print(f"{symbol}: {old} -> {new}")


class AlertWhenAbove:
    def __init__(self, limit):
        self.limit = limit

    def __call__(self, symbol, old, new):
        if new > self.limit:
            print(f"ALERT {symbol} above {self.limit}")


if __name__ == "__main__":
    ticker = StockTicker("ACME", 100)
    ticker.subscribe(print_change)
    ticker.subscribe(AlertWhenAbove(110))
    ticker.price = 105
    ticker.price = 112
    ticker.unsubscribe(print_change)
    ticker.price = 90
    ticker.price = 120
```

Output:

```text
ACME: 100 -> 105
ACME: 105 -> 112
ALERT ACME above 110
ALERT ACME above 110
```

Now try it yourself: **T10-E07** in `exercises.md`.

---

## 8. Decorator

**In one sentence:** Add behaviour to an object by wrapping it in another object with the same interface.

**Use it when:**

- You want optional, combinable features (logging, retry, compression, encryption, caching) without a subclass for every combination.
- The extra behaviour must be chosen at run time.

**Be careful:**

- This is not the same as Python's `@decorator` syntax, which wraps functions; the ideas are related but the pattern wraps objects.
- Every wrapper must keep the same interface, otherwise stacking breaks.

**Python-flavoured implementation:** a wrapper class that stores the inner object and forwards calls (`__getattr__` can forward the rest); wrappers are stacked by passing one into another.

Runnable demo: `examples/p08_decorator_pattern.py` (run it with `python examples/p08_decorator_pattern.py`).

```python
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
```

Output:

```text
Uryyb Jbeyq
Hello World
400 True
True
```

Now try it yourself: **T10-E08** in `exercises.md`.

---

## 9. Command

**In one sentence:** Turn an action into an object, so it can be stored, queued, logged, undone and redone.

**Use it when:**

- You need undo/redo, a history of actions, macros or a job queue.
- You want to separate who triggers an action from how it is done (buttons, remote controls, menus).

**Be careful:**

- A command must remember enough state to undo itself (for example, the text it deleted).
- For simple one-shot callbacks a plain function or `functools.partial` is enough.

**Python-flavoured implementation:** a class with `execute()` and `undo()` methods plus a history list; simple commands without undo can be plain callables.

Runnable demo: `examples/p09_command.py` (run it with `python examples/p09_command.py`).

```python
"""Command worked example: a smart-light remote with undo."""


class Light:
    def __init__(self):
        self.on = False
        self.level = 0


class TurnOn:
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.previous = (self.light.on, self.light.level)
        self.light.on, self.light.level = True, 100

    def undo(self):
        self.light.on, self.light.level = self.previous


class Dim:
    def __init__(self, light, level):
        self.light = light
        self.level = level

    def execute(self):
        self.previous = (self.light.on, self.light.level)
        self.light.on, self.light.level = True, self.level

    def undo(self):
        self.light.on, self.light.level = self.previous


class Remote:
    def __init__(self):
        self.history = []

    def press(self, command):
        command.execute()
        self.history.append(command)

    def undo(self):
        if self.history:
            self.history.pop().undo()


if __name__ == "__main__":
    light, remote = Light(), Remote()
    remote.press(TurnOn(light))
    print(light.on, light.level)
    remote.press(Dim(light, 30))
    print(light.on, light.level)
    remote.undo()
    print(light.on, light.level)
    remote.undo()
    print(light.on, light.level)
    remote.undo()
    print("history empty:", not remote.history)
```

Output:

```text
True 100
True 30
True 100
False 0
history empty: True
```

Now try it yourself: **T10-E09** in `exercises.md`.

---

## 10. Iterator

**In one sentence:** Provide a standard way to walk through a collection one item at a time without exposing how it is stored.

**Use it when:**

- You want `for` loops to work with your own classes.
- Data is large, infinite or fetched lazily (database rows, API pages, files) and should not be loaded all at once.

**Be careful:**

- An iterator is used up after one pass; make your container an iterable that returns a new iterator on each `iter()` call.
- Do not write the `__next__` class by hand if a generator function is enough.

**Python-flavoured implementation:** implement `__iter__` and `__next__` (raising `StopIteration` at the end), or just write a generator function with `yield`; `yield from` delegates to a sub-generator.

Runnable demo: `examples/p10_iterator.py` (run it with `python examples/p10_iterator.py`).

```python
"""Iterator worked example: the iterator protocol and its generator shortcut."""


class Countdown:
    """Hand-written iterator: __iter__ returns self, __next__ returns the next value."""

    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def countdown_gen(start):
    """The same thing as a generator: yield replaces the bookkeeping."""
    while start > 0:
        yield start
        start -= 1


class Playlist:
    """An iterable container: every `for` loop gets a fresh, independent iterator."""

    def __init__(self, songs):
        self.songs = list(songs)

    def __iter__(self):
        return iter(self.songs)


if __name__ == "__main__":
    print(list(Countdown(3)))
    print(list(countdown_gen(3)))
    it = Countdown(2)
    print(next(it), next(it))
    try:
        next(it)
    except StopIteration:
        print("exhausted")
    playlist = Playlist(["intro", "song", "outro"])
    print([s.upper() for s in playlist])
    print(len(list(playlist)), len(list(playlist)))
```

Output:

```text
[3, 2, 1]
[3, 2, 1]
2 1
exhausted
['INTRO', 'SONG', 'OUTRO']
3 3
```

Now try it yourself: **T10-E10** in `exercises.md`.
