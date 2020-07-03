
import numpy as np

from Enviroment.phisical_properties import Position
from Enviroment.piste import Piste, Gate
from Enviroment.run import Run
from Skier.ai_skier import AISkier
from Training.training_run import TrainingRun
from Skier.random_skier import RandomSkier
from Training.trainer import AITrainer

REWARD = 1
REWARD_OUT = -1
SAMPLE_SIZE = 250
CAPACITY = 10000
GAMMA = 0.99
EPS_MIN = 0.001
EPS_DECAY = 0.0001
UPDATE_TARGET_EVERY = 100
RUNS = 100_000

#, Position(1,7)
gates = [Gate(range(1,3),5),Gate(range(7,10),12), Gate(range(1,4),19), Gate(range(7,9),24), Gate(range(2,8),29)]

initial = Position(5,0)
p = Piste(10,30,initial, gates)
s = AITrainer(REWARD, REWARD_OUT, SAMPLE_SIZE, CAPACITY, GAMMA, EPS_MIN, EPS_DECAY, UPDATE_TARGET_EVERY)
training_run = TrainingRun(p, s)

counter = 0
fifty = 0
for i in range(RUNS):
    training_run.run()
    counter += training_run.result
    s.update_eps(i)
    if i % 50 == 0 and i > 0:
        print(i, counter, s.eps_greedy_value, s.model_network.loss, )

        if counter == 50:
            fifty += 1
        else:
            fifty = 0
        if fifty == 10:
            break
        counter = 0

s.trajectory.print()
s.target_network.save_weights("data/trained")

ai = AISkier("data/trained.pt")
run = Run(p, ai)
run.run()
ai.trajectory.print()
