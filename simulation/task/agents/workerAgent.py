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
    def __init__(self, worker_id, model):
        super().__init__(worker_id, model)
        # Params
        self.fatigue_tolerance = 1
        self.emails_read = 0
        self.average_daily_tasks = 0
        self.daily_tasks_total = 0
        self.daily_tasks_number = 0
        self.daily_tasks_time = 0
        self.daily_emails_number = 0
        self.rest_daily_time = 0
        self.overtime_daily_time = 0
        self.email_read_time = 0
        self.productivity = 1

        # Stress params
        self.time_pressure = 0
        self.event_stress = 0.1
        self.effective_fatigue = 0
        self.stress = 0

        # Pending work
        self.emails = []
        self.tasks = []


    def work_in_task(self):

        # select a task to work in
        current_task = self.tasks[0]

        # work in the task selected
        current_task.time -= self.productivity*configuration.settings.time_by_step/60

        # check if the task has finished
        if current_task.time <= 0:
            self.tasks.pop(0)
            current_task = None

    def receive_email(self, email):
        self.email_read_time += email.read_estimated_time
        self.emails.remove(email)
        self.model.schedule.remove(email)
        # add stress
        self.effective_fatigue += 0.0028699

    def step(self):

        # check if it is work titme
        is_work_time = configuration.settings.workersTiming['arrivalTime'] <= self.model.time.clock < configuration.settings.workersTiming['leavingTime']
        is_overtime = configuration.settings.workersTiming['leavingTime'] <= self.model.time.clock < configuration.settings.workersTiming['overtimeLimit']
        is_sleep_time = configuration.settings.workersTiming['sleepStart'] <= self.model.time.clock < configuration.settings.workersTiming['sleepEnd']
        self.effective_fatigue = min(self.effective_fatigue, 1)

        if self.model.new_day:

            # receive daily emails
            if self.model.spike_day:
                self.daily_emails_number = 2*math.floor(abs(self.model.email_read_distribution[random.randint(0, 10*self.model.num_agents-1)]))
            else:
                self.daily_emails_number = math.floor(abs(self.model.email_read_distribution[random.randint(0, 10*self.model.num_agents-1)]))

            for i in range(1, self.daily_emails_number):
                self.emails.extend([Email(self.model, self)])

            # receive daily tasks
            self.average_daily_tasks = 0

            ## asign the number of tasks for the worker for today
            self.daily_tasks_number = math.floor(abs(self.model.tasks_arriving_distribution[random.randint(0, 10*self.model.num_agents-1)]))
            self.daily_tasks_total += self.daily_tasks_number

            ## create tasks
            for i in range(1, self.daily_tasks_number):
                self.tasks.extend([Task()])

            # calculate stress

            self.daily_tasks_time = 0

            ## calculate estimated time for tasks
            for task in self.tasks:
                self.daily_tasks_time += task.time

            ## calculate time pressure
            self.time_pressure = self.daily_tasks_time/(self.daily_tasks_time + (configuration.settings.workersTiming['leavingTime'].hour-self.model.time.hours)*60)

            ## calculate event stress
            self.event_stress = self.daily_tasks_number/2/20
            #print("Event stress:" + str(self.event_stress))

            #self.model.log.collectStress(str(self.model.time.clock.hour) + ":" + str(self.model.time.clock.minute), self.unique_id, self.effective_fatigue)
            #print("Time pressure:" + str(self.time_pressure))

            ## calculate effective fatigue
            self.effective_fatigue += (self.overtime_daily_time/60*0.01054+0.4536) - (self.rest_daily_time/60*self.effective_fatigue)/10
            self.rest_daily_time = 0
            self.overtime_daily_time = 0

            # calculate total stress
            self.stress = (self.event_stress + self.time_pressure + self.effective_fatigue)/3

            if self.stress <= 0.2:
                self.productivity = 0.5
            elif self.stress > 0.2 and self.stress <= 0.4:
                self.productivity = 1
            elif self.stress > 0.4 and self.stress <= 0.6:
                self.productivity = 1.5
            elif self.stress > 0.6 and self.stress <= 0.8:
                self.productivity = 1
            else:
                self.productivity = 0.5

        #print("Event stress:" + str(self.event_stress))
        #print("Time pressure:" + str(self.time_pressure))
        #print("Effective fatigue:" + str(self.effective_fatigue))

        if is_work_time:

            # check if there is unread emails
            if self.email_read_time > 0:
                self.email_read_time -= 1
            else:
                # check if there are remaining tasks
                if len(self.tasks) > 0:
                    self.work_in_task()
                else:
                    self.rest_daily_time += 1
        elif is_overtime:
            if len(self.tasks) > 0:
                self.work_in_task()
                self.overtime_daily_time += 1
        elif is_sleep_time:
            if len(self.tasks) > 5:
                self.work_in_task()
                self.overtime_daily_time += 1
            else:
                self.rest_daily_time += 1
            #print("Number of tasks for agent " + str(self.unique_id) + ": " + str(self.daily_tasks_total))

        # check if should add a new task
        #if len(self.tasks) == 0:
        #    self.tasks.extend([Task()])
        # check if the day has changed, if true, add new daily tasks
        #if self.day != self.model.time.days and self.model.time.clock.hour == 9:
        #    for i in range(random.randint(7, 10)):
        #        if len(self.tasks) < 14:
        #            self.tasks.extend([Task()])
        #    self.day = self.model.time.days
        #    return

        #if len(self.emails) < self.emails_by_day:
        #    self.emails.extend([Email()])

        # receive (or not) a new email
        #if random.random() < configuration.settings.new_email_prob:
        #    self.emails.extend([Email()])

        # calculate remaining work time
        #if is_work_time:
            #print("Work time")
            # automate (or not) a task
            #if self.model.automationPlatform.automate_tasks:
            #    if random.random() < configuration.settings.automate_task_prob:
            #        if len(self.tasks) > 0:
            #            self.tasks.pop(0)

            # calculate remaining task time in minutes
            #remaining_tasks_time = 0

            #for task in self.tasks:
            #    remaining_tasks_time += task.time

            #remaining_work_time = datetime.combine(date.min, configuration.settings.workersTiming['leavingTime']) - datetime.combine(date.min, self.model.time.clock)
            #remaining_work_time_minutes = remaining_work_time.seconds / 60

            #print("Remaining work time for agent " + str(self.unique_id) + ": " + str(remaining_work_time_minutes))

            # calculate stress
            #if remaining_work_time_minutes != 0:
            #    self.stress = min(10, math.ceil(self.base_stress + (1 - self.stress_tolerance)*math.pow(1.5, math.sqrt((len(self.tasks)+remaining_tasks_time/remaining_work_time_minutes)*configuration.settings.max_stress/configuration.settings.real_max_stress))))
                #print("Stress for agent " + str(self.unique_id) + ": " + str(self.stress))
        #else:
        #    print("Not working")
            #if len(self.tasks) > 0:
            #    self.base_stress = len(self.tasks)*self.responsibility
            #else:
            #    self.base_stress = 0

        # check if there are remaining tasks, and select current task
        #if len(self.tasks) > 0:
        #    self.currentTask = self.tasks[0]
        #else:
            # if there aren't tasks, spend time reading email
        #    for email in self.emails:
        #        if email.contains_task:
        #            self.tasks.extend([Task()])
        #        self.emails.remove(email)
        #    return

        # check if the worker is in work time, if true, work in a task
        #if is_work_time:

            # if there are a lot of emails, spend time reading them and not doing tasks
            #if len(self.emails) > 15:
            #    for email in self.emails:
            #        if email.contains_task:
            #            self.tasks.extend([Task()])
            #        self.emails.remove(email)
            #        return

            #self.currentTask.time -= self.minutesByStep

            # duplicate productivity
            #if self.currentTask.time > self.minutesByStep and random.random() < self.productivity:
            #    self.currentTask.time -= self.minutesByStep

            # if task has been finished, remove it
            #if self.currentTask.time == 0:
            #    self.tasks.pop(0)

        #print("Remaining task time for agent " + str(self.unique_id) + ": " + str(remaining_tasks_time))
        #print("Remaining tasks for agent " + str(self.unique_id) + ": " + str(len(self.tasks)))
        #print("Stress for agent " + str(self.unique_id) + ": " + str(self.stress))
        # self.stress += randint(0,10)
        # self.model.log.collectStress(str(self.model.time.clock.hour) + ":" + str(self.model.time.clock.minute), self.unique_id, self.stress)
