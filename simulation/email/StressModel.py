from StressAgent import StressAgent
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random
from mesa.datacollection import DataCollector

class StressModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)
        # Create agents
        for i in range(self.num_agents):
            a = StressAgent(i, self)
            self.schedule.add(a)

        self.datacollector = DataCollector(
            agent_reporters={"Stress": lambda a: a.stress, "AutomatedEmails" : lambda a: a.automated_emails})

    def step(self):
        '''Advance the model by one step.'''
        self.datacollector.collect(self)
        self.schedule.step()