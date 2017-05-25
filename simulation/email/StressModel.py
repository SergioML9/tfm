from StressAgent import StressAgent
from NewAgent import NewAgent
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
        self.workers = []
        # Create agents
        for i in range(self.num_agents):
            a = StressAgent(i, self)
            self.workers.append(a)
            self.schedule.add(a)
        self.schedule.add(NewAgent(5823, self))
        self.datacollector = DataCollector(
            agent_reporters={"Stress": lambda a: a.stress if isinstance(a, StressAgent) else -1, "Queue": lambda b : b.queue if isinstance(b, NewAgent) else -1})

    def step(self):
        '''Advance the model by one step.'''
        self.datacollector.collect(self)
        self.schedule.step()
