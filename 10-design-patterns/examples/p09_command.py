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
