from Enviroment.phisical_properties import Position
from Enviroment.physics import Physics, Trajectory
from Enviroment.piste import Piste
from Skier.skier import Skier
import copy


class Run:

    def __init__(self, piste: Piste, skier: Skier):
        self.physics = Physics()
        self.piste = piste
        self.trajectory = Trajectory(self.piste)
        self.skier = skier
        self.t = 0
        self.result = None

    def run(self):
        state = self.piste.get_initial_state()
        ended = False
        while not ended:
            action = self.skier.get_action(state)
            self.trajectory.add(state.position)
            next_state = self.physics.get_next_state(state, action)
            if self.out(next_state.position):
                self.result = False
                self.trajectory.add(state.position)
                self.skier.trajectory = copy.copy(self.trajectory)
                return

            if self.ended(next_state.position):
                self.result = True
                ended = True
                state = next_state
            else:
                state = next_state

        self.trajectory.add(state.position)
        self.skier.trajectory = copy.copy(self.trajectory)
        self.trajectory.reset()

    def out(self, position: Position):
        return self.piste.out(position)

    def ended(self, position: Position):
        return self.piste.ended(position)

