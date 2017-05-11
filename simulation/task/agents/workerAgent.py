from mesa import Agent
import random
from random import randint
import math
from classes.task import Task
import configuration.settings

class WorkerAgent(Agent):

    """ An agent with fixed initial wealth."""
    def __init__(self, worker_id, model):
        super().__init__(worker_id, model)
        self.stress = random.uniform(0, 1)
        self.day = -1
        self.tasks = []

    def step(self):

        if self.day != self.model.time.days:
            self.tasks.extend([Task(), Task(), Task(), Task(), Task(), Task(), Task(), Task()])
            self.day = self.model.time.days

        if len(self.tasks) > 0:
            self.currentTask = self.tasks[0]
        else:
            return

        if configuration.settings.workersTiming['arrivalTime'] <= self.model.time.clock <= configuration.settings.workersTiming['leavingTime']:
            self.currentTask.time -= configuration.settings.time_by_step/60
            if self.currentTask.time == 0:
                self.tasks.pop(0)

        print("Remaining tasks for agent " + str(self.unique_id) + ": " + str(len(self.tasks)))
        #self.stress += randint(0,10)
        #self.model.log.collectStress(str(self.model.time.clock.hour) + ":" + str(self.model.time.clock.minute), self.unique_id, self.stress)
