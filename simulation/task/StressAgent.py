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
        
        beta = 0.1
        alpha = 0.05
        t = randint(0,500)
        self.stress = math.floor(math.pow(alpha * t, 2))
        
