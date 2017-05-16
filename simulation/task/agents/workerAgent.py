from mesa import Agent
import random
from random import randint
import math
from classes.task import Task
import configuration.settings
from datetime import datetime, date

class WorkerAgent(Agent):

    """ An agent with fixed initial wealth."""
    def __init__(self, worker_id, model):
        super().__init__(worker_id, model)
        self.base_stress = random.uniform(0, 1)
        self.stress_tolerance = random.uniform(0, 1)
        self.day = -1
        self.tasks = []
        self.productivity = random.choice(configuration.settings.productivity_probs)
        self.minutesByStep = configuration.settings.time_by_step/60
        self.stress = 0

    def step(self):

        # check if is work titme
        is_work_time = configuration.settings.workersTiming['arrivalTime'] <= self.model.time.clock <= configuration.settings.workersTiming['leavingTime']
        
        # check if the day has changed, if true, add new daily tasks
        if self.day != self.model.time.days and self.model.time.clock.hour == 9:
            for i in range(random.randint(6, 10)):
                self.tasks.extend([Task()])
            self.day = self.model.time.days
            return

        # calculate remaining task time in minutes
        remaining_tasks_time = 0

        for task in self.tasks:
            remaining_tasks_time += task.time

        # calculate remaining work time
        if is_work_time:
            remaining_work_time = datetime.combine(date.min, configuration.settings.workersTiming['leavingTime']) - datetime.combine(date.min, self.model.time.clock)
            remaining_work_time_minutes = remaining_work_time.seconds / 60

            # calculate stress
            if remaining_work_time_minutes != 0:
                self.stress = self.base_stress + (1 - self.stress_tolerance)*math.pow(math.e, remaining_tasks_time/remaining_work_time_minutes)
        
        # check if there are remaining tasks, and select current task
        if len(self.tasks) > 0:
            self.currentTask = self.tasks[0]
        else:
            return

        # check if the worker is in work time, if true, work in a task
        if is_work_time:
            self.currentTask.time -= self.minutesByStep

            # duplicate productivity
            if self.currentTask.time > self.minutesByStep and random.random() < self.productivity:
                self.currentTask.time -= self.minutesByStep

            # if task has been finished, remove it
            if self.currentTask.time == 0:
                self.tasks.pop(0)

        print("Remaining task time for agent " + str(self.unique_id) + ": " + str(remaining_tasks_time))
        print("Remaining work time for agent " + str(self.unique_id) + ": " + str(remaining_work_time_minutes))
        print("Remaining tasks for agent " + str(self.unique_id) + ": " + str(len(self.tasks)))
        print("Stress for agent " + str(self.unique_id) + ": " + str(self.stress))
        # self.stress += randint(0,10)
        # self.model.log.collectStress(str(self.model.time.clock.hour) + ":" + str(self.model.time.clock.minute), self.unique_id, self.stress)
