import numpy as np


class Position:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def copy(self):
        return Position(self.x, self.y)


class PhysicalProperties:

    def __init__(self, position: Position, v: np.array):
        self.position = position
        self.v = v

    def copy(self):
        return PhysicalProperties(self.position.copy(),self.v.copy())


