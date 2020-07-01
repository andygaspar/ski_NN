from Enviroment.phisical_properties import PhysicalProperties, Position
from Enviroment.piste import Piste


class Physics:

    def __init__(self):
        self.no_obj = ""

    def get_next_state(self, state: PhysicalProperties, action: float) -> PhysicalProperties:
        self.no_obj = ""
        if action == 0:
            return PhysicalProperties(Position(state.position.x, state.position.y + 1), state.v)
        if action == 1:
            return PhysicalProperties(Position(state.position.x + 1, state.position.y + 1), state.v)
        if action == -1:
            return PhysicalProperties(Position(state.position.x - 1, state.position.y + 1), state.v)


class Trajectory:

    def __init__(self, piste: Piste):
        self.trajectory = []
        self.piste = piste

    def add(self, position: Position):
        self.trajectory.append(position.copy())

    def print(self):
        for i in range(len(self.trajectory)):
            line = ""
            for j in range(self.piste.width):
                line += "* "
            line = line[:self.trajectory[i].x*2] + "X " + line[(self.trajectory[i].x*2)+2:]
            print(line)
        print("\n")

    def reset(self):
        self.trajectory = []
