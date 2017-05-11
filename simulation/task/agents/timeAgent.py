from mesa import Agent, Model
import configuration.settings
import math
import datetime

class Time(Agent):

    def __init__(self):

        #print(configuration.settings.workersTiming['arriveTime'])
        self.timeByStep = configuration.settings.time_by_step
        self.clock = datetime.time(8, 00)
        self.days = 0
        self.hours = self.clock.hour
        self.minutes = self.clock.minute
        self.seconds = self.clock.second-self.timeByStep

    def step(self):
        self.seconds = self.seconds + self.timeByStep
        if self.seconds > 59:
            self.minutes = self.minutes + math.floor(self.seconds/60)
            self.seconds = 0
            #self.seconds = self.seconds + self.seconds % 60
            if self.minutes > 59:
                self.hours = self.hours + math.floor(self.minutes/60)
                self.minutes = 0
                #self.minutes = self.minutes + self.minutes % 60
                if self.hours > 23:
                    self.days = self.days + math.floor(self.hours/24)
                    self.hours = 0
                #    self.hours = self.hours + self.hours % 24

        #self.clock = (self.hour*100 + self.minute) / 100
        self.clock = datetime.time(self.hours,self.minutes)
        print('Day: ', (self.days + 1), ' - Hour: ', self.clock)
