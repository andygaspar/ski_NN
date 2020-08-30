import numpy as np

from Enviroment.phisical_properties import Position
from Enviroment.phisical_properties import PhysicalProperties


class Gate:

    def __init__(self, gate: range, y: int):
        self.y = y
        self.x = [i for i in gate]


class Piste:
    piste: np.ndarray
    length: int
    width: int

    def __init__(self,  width: int, length: int, initial: Position, gates: list):
        self.width = width
        self.length = length
        self.gates = gates[:-1]
        self.piste = np.zeros((self.length, self.width)).astype(int)
        self.initial = initial
        self.final = gates[-1]

    def get_initial_state(self):
        return PhysicalProperties(self.initial, np.zeros(2))

    def ended(self, position: Position):
        if position.y == self.length-1 and position.x in self.final.x:
            return True
        else:
            return False

    def out(self, position: Position):
        if position.x < 0 or position.x > self.width or position.y > self.length:
            return True
        return False

    def missed_gate(self, position: Position):
        gates = self.gates
        gates.append(self.final)
        for gate in gates:
            if position.y == gate.y and position.x not in gate.x:
                return True
        return False

    def print(self):
        for i in range(self.length):
            line = ""
            for j in range(self.width):
                line += str(self.piste[i,j]) + " "
            print(line)


