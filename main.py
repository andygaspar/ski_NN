
import numpy as np

from Enviroment.phisical_properties import Position
from Enviroment.piste import Piste
from Enviroment.run import Run
from Skier.random_skier import RandomSkier
from Training.trainer import AITrainer

REWARD = 1
REWARD_OUT = -1
SAMPLE_SIZE = 100
CAPACITY = 10000
GAMMA = 0.99
EPS_MIN = 0
EPS_DECAY = 0.001
UPDATE_TARGET_EVERY = 100


gates = [Position(3,3), Position(1,7)]

initial = Position(2,0)
final = np.array([2])
p = Piste(5,10,initial, final, gates)
s = AITrainer(REWARD, REWARD_OUT, SAMPLE_SIZE, CAPACITY, GAMMA, EPS_MIN, EPS_DECAY, UPDATE_TARGET_EVERY)
run = Run(p, s)

counter = 0
fifty = 0
for i in range(20000):
    run.run()
    counter += run.result
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

