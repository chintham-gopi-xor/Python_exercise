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
