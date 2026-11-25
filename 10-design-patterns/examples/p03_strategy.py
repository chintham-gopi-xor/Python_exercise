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
