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
