import numpy as np
from Enviroment.phisical_properties import PhysicalProperties
from Skier.skier import Skier


class RandomSkier(Skier):

    def __init__(self):
        super().__init__()

    def get_action(self, state: PhysicalProperties) -> int:
        #return 0
        return np.random.choice([1,0,-1])
