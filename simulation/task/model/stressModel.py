from agents.stressAgent import StressAgent
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random
from mesa.datacollection import DataCollector
from agents.timeAgent import Time

class StressModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.schedule = RandomActivation(self)

        # Create control of time
        self.clock = Time()
        self.schedule.add(self.clock)

        # Create agents
        for i in range(self.num_agents):
            a = StressAgent(i, self)
            self.schedule.add(a)

        self.datacollector = DataCollector(
            agent_reporters={"Stress": lambda a: a.stress})

    def step(self):
        '''Advance the model by one step.'''
        self.datacollector.collect(self)
        self.schedule.step()
