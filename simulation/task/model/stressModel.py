from agents.workerAgent import WorkerAgent
from mesa import Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
import random
from mesa.datacollection import DataCollector
from agents.timeAgent import Time
from log.log import CustomLog
from agents.automationPlatformAgent import AutomationPlatformAgent
import configuration.settings
import numpy
import math

class StressModel(Model):
    """A model with some number of agents."""
    def __init__(self, N):
        self.num_agents = N
        self.current_step = 0

        self.schedule = RandomActivation(self)
        self.users = []

        # Create automation platform
        self.automationPlatform = AutomationPlatformAgent();

        # Create log
        self.log = CustomLog()
        self.log.initCollectStress()

        # Create control of time
        self.time = Time()
        self.schedule.add(self.time)

        # Create distribution of emails read
        mu, sigma = configuration.settings.emails_read_distribution_params
        email_read_distribution = numpy.random.normal(mu, sigma, N)

        # Create agents
        for i in range(self.num_agents):
            a = WorkerAgent(i, self, math.floor(abs(email_read_distribution[i])))
            self.schedule.add(a)
            self.users.append(a)

        #self.datacollector = DataCollector(
        #    agent_reporters={"Stress": lambda a: a.stress})

    def step(self):
        '''Advance the model by one step.'''
        self.current_step += 1
        self.schedule.step()
