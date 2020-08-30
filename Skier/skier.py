from abc import abstractmethod
from Enviroment.phisical_properties import PhysicalProperties, Position
import numpy as np


class Skier:

    def __init__(self):
        self.trajectory = None

    @abstractmethod
    def get_action(self, state: PhysicalProperties) -> int:
        pass

    @abstractmethod
    def add_record(self, next_state: PhysicalProperties, done: bool):
        pass

    @abstractmethod
    def end(self):
        pass

    @abstractmethod
    def out(self):
        pass

    def gate_done(self, next_state: PhysicalProperties):
        pass
