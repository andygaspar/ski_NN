# from Skier.AIPlayer import AIPlayer
import string

from Enviroment.phisical_properties import PhysicalProperties
from Skier.skier import Skier
from Training.network import Network
import numpy as np
from Training.replayMemory import ReplayMemory


class AISkier(Skier):

    def __init__(self, filename: string):

        super().__init__()
        self.net = Network(4)
        self.net.load_weights(filename)
        self.net.network.eval()

    def get_action(self, state: PhysicalProperties) -> int:
        state = self.get_state(state)
        action = self.net.get_action(state)
        return self.convert_action(action)

    def get_state(self, state: PhysicalProperties):
        return np.array([state.position.x, state.position.y, state.v[0], state.v[1]])

    def convert_action(self, action):
        if action == 0:
            return -1
        if action == 1:
            return 0
        if action == 2:
            return 1
