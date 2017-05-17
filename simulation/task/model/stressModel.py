from agents.workerAgent import WorkerAgent
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random
from mesa.datacollection import DataCollector
from agents.timeAgent import Time
from log.log import CustomLog

class StressModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.current_step = 0
        
        self.schedule = RandomActivation(self)
        self.users = []

        # Create log
        self.log = CustomLog()
        self.log.initCollectStress()

        # Create control of time
        self.time = Time()
        self.schedule.add(self.time)

        # Create agents
        for i in range(self.num_agents):
            a = WorkerAgent(i, self)
            self.schedule.add(a)
            self.users.append(a)

        #self.datacollector = DataCollector(
        #    agent_reporters={"Stress": lambda a: a.stress})

    def step(self):
        '''Advance the model by one step.'''
        self.current_step += 1
        self.schedule.step()
