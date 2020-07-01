import numpy as np

from Enviroment.phisical_properties import Position
from Enviroment.phisical_properties import PhysicalProperties


class Piste:
    piste: np.ndarray
    length: int
    width: int

    def __init__(self,  width: int,length: int, initial: Position, final: np.array, gates: list = []):
        self.width = width
        self.length = length
        self.gates = gates
        self.piste = np.zeros((self.length, self.width)).astype(int)
        self.initial = initial
        self.final = final

    def get_initial_state(self):
        return PhysicalProperties(self.initial, np.zeros(2))

    def ended(self, position: Position):
        if position.y == self.length-1 and position.x in self.final:
            return True
        else:
            return False

    def out(self, position: Position):
        if position.x < 0 or position.x > self.width or position.y > self.length:
            return True
        missed = self.missed_gate(position)
        return missed

    def missed_gate(self, position: Position):
        for gate in self.gates:
            if position.y == gate.y and position.x != gate.x:
                return True
            else:
                return False
        
    def print(self):
        for i in range(self.length):
            line = ""
            for j in range(self.width):
                line += str(self.piste[i,j]) + " "
            print(line)


