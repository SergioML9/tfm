from mesa import Agent
import configuration.settings
import numpy
import math
import random

class Email(Agent):

    def __init__(self, model, worker):
        super().__init__(worker.unique_id*100, model)
        self.model = model
        self.worker = worker
        mu, sigma = configuration.settings.email_time_reception_distribution_params
        self.reception_time = math.floor(abs(numpy.random.normal(mu, sigma, 100)[random.randint(0, 99)]))
        mu, sigma = configuration.settings.email_read_time_distribution_params
        self.read_estimated_time = math.floor(abs(numpy.random.normal(mu, sigma, 10)[random.randint(0,9)]))

        if self.reception_time < 10 or self.reception_time > 17:
            self.reception_time = 10

        self.model.schedule.add(self)

    def step(self):
        if self.model.time.hours == self.reception_time:
            self.worker.receive_email(self)
