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
