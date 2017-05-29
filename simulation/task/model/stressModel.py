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
        self.running = True

        self.schedule = RandomActivation(self)
        self.workers = []

        # Create automation platform
        self.automationPlatform = AutomationPlatformAgent();

        # Create log
        self.log = CustomLog()
        self.log.initCollectStress()

        # Create control of time
        self.time = Time(self)
        self.new_day = False
        self.new_hour = False
        self.schedule.add(self.time)

        # Create distribution of emails read
        mu, sigma = configuration.settings.emails_read_distribution_params
        self.email_read_distribution = numpy.random.normal(mu, sigma, N*10)

        # Create distribution of fatigue tolerance
        mu, sigma = configuration.settings.fatigue_tolerance_distribution_paramas
        fatigue_tolerance_distribution = numpy.random.normal(mu, sigma, N)

        # Create distribution of tasks distribution
        mu, sigma = configuration.settings.tasks_arriving_distribution_params
        self.tasks_arriving_distribution = numpy.random.normal(mu, sigma, N*10)

        # Create agents
        for i in range(self.num_agents):
            a = WorkerAgent(i, self)

            # Assign params
            a.fatigue_tolerance = math.floor(abs(fatigue_tolerance_distribution[i]))
            self.schedule.add(a)
            self.workers.append(a)

        # Create workplace management
        self.spike_day = False

    def step(self):
        '''Advance the model by one step.'''

        self.spike_day = False
        # Update new day
        if self.time.hours == 9 and self.time.minutes == 0:
            self.new_day = True
            if random.random() < 0.05 and self.time.days != 0:
                self.spike_day = True
        else:
            self.new_day = False

        if self.time.minutes == 0:
            self.new_hour = True
        else:
            self.new_hour = False

        self.current_step += 1
        self.schedule.step()
