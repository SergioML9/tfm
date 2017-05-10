from mesa import Agent
import random
from random import randint
import math

class StressAgent(Agent):

    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.stress = 0

    def step(self):
        self.stress += randint(0,10)
        self.model.log.collectStress(self.model.clock.clock, self.unique_id, self.stress)
