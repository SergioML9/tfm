from mesa import Agent
import random
from random import randint
import math

class NewAgent(Agent):

    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.queue = 0


    def step(self):
        self.queue = 5
