from mesa import Agent
import random
from random import randint
import math
from classes.task import Task
from classes.email import Email
import configuration.settings
from datetime import datetime, date

class WorkerAgent(Agent):

    """ An agent with fixed initial wealth."""
    def __init__(self, worker_id, model, emails_read):
        super().__init__(worker_id, model)
        self.base_stress = random.uniform(0, 1)
        self.stress_tolerance = random.uniform(0, 0.5)
        self.responsibility = random.uniform(0, 0.8)
        self.day = -1
        self.emails = []
        self.tasks = []
        self.productivity = random.choice(configuration.settings.productivity_probs)
        self.minutesByStep = configuration.settings.time_by_step/60
        self.stress = 0
        #print("Agent " + str(worker_id) + " reads " + str(emails_read) + " by day.")

    def step(self):

        # check if is work titme
        is_work_time = configuration.settings.workersTiming['arrivalTime'] <= self.model.time.clock <= configuration.settings.workersTiming['leavingTime']

        # check if the day has changed, if true, add new daily tasks
        if self.day != self.model.time.days and self.model.time.clock.hour == 9:
            for i in range(random.randint(7, 10)):
                if len(self.tasks) < 14:
                    self.tasks.extend([Task()])
            self.day = self.model.time.days

            return

        # receive (or not) a new email
        if random.random() < configuration.settings.new_email_prob:
            self.emails.extend([Email()])

        # calculate remaining work time
        if is_work_time:

            # automate (or not) a task
            if self.model.automationPlatform.automate_tasks:
                if random.random() < configuration.settings.automate_task_prob:
                    if len(self.tasks) > 0:
                        self.tasks.pop(0)

            # calculate remaining task time in minutes
            remaining_tasks_time = 0

            for task in self.tasks:
                remaining_tasks_time += task.time

            remaining_work_time = datetime.combine(date.min, configuration.settings.workersTiming['leavingTime']) - datetime.combine(date.min, self.model.time.clock)
            remaining_work_time_minutes = remaining_work_time.seconds / 60

            #print("Remaining work time for agent " + str(self.unique_id) + ": " + str(remaining_work_time_minutes))

            # calculate stress
            if remaining_work_time_minutes != 0:
                self.stress = min(10, math.ceil(self.base_stress + (1 - self.stress_tolerance)*math.pow(1.5, math.sqrt((len(self.tasks)+remaining_tasks_time/remaining_work_time_minutes)*configuration.settings.max_stress/configuration.settings.real_max_stress))))
                #print("Stress for agent " + str(self.unique_id) + ": " + str(self.stress))
        else:
            if len(self.tasks) > 0:
                self.base_stress = len(self.tasks)*self.responsibility
            else:
                self.base_stress = 0

        # check if there are remaining tasks, and select current task
        if len(self.tasks) > 0:
            self.currentTask = self.tasks[0]
        else:
            # if there aren't tasks, spend time reading email
            for email in self.emails:
                if email.contains_task:
                    self.tasks.extend([Task()])
                self.emails.remove(email)
            return

        # check if the worker is in work time, if true, work in a task
        if is_work_time:

            # if there are a lot of emails, spend time reading them and not doing tasks
            if len(self.emails) > 15:
                for email in self.emails:
                    if email.contains_task:
                        self.tasks.extend([Task()])
                    self.emails.remove(email)
                    return

            self.currentTask.time -= self.minutesByStep

            # duplicate productivity
            if self.currentTask.time > self.minutesByStep and random.random() < self.productivity:
                self.currentTask.time -= self.minutesByStep

            # if task has been finished, remove it
            if self.currentTask.time == 0:
                self.tasks.pop(0)

        #print("Remaining task time for agent " + str(self.unique_id) + ": " + str(remaining_tasks_time))
        #print("Remaining tasks for agent " + str(self.unique_id) + ": " + str(len(self.tasks)))
        #print("Stress for agent " + str(self.unique_id) + ": " + str(self.stress))
        # self.stress += randint(0,10)
        # self.model.log.collectStress(str(self.model.time.clock.hour) + ":" + str(self.model.time.clock.minute), self.unique_id, self.stress)
