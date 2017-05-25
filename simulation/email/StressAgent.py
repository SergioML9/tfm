from mesa import Agent
import random
from random import randint
import math


def compute_stress(model):
    return self.stress

class StressAgent(Agent):

    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.queue = 0
        self.stress = 0
        self.alpha = 2
        self.automate_read = 1
        self.automate_task = 0
        self.automated_emails = 0
        self.automated_tasks = 0

    def step(self):
        emails_received = randint(0, 5)
        self.alpha = 2

        task_queue = 0

        task_automation_ratio = 0.25
        automated_emails_ratio = 0.25

        for i in range(emails_received):

            # Añado automatización de lectura
            if self.automate_read and random.random() <= automated_emails_ratio:
                self.alpha += 1
                self.automated_emails += 1

            if randint(0,4) == 0:
                # Añado automatización de tareas
                if self.automate_task:
                    if random.random() > task_automation_ratio:
                        task_queue += 5
                    else:
                        self.automated_tasks += 1
                else:
                    task_queue += 5

        emails_queue = emails_received - self.alpha

        self.queue += (emails_queue + task_queue)
        self.stress = min(max(math.floor(self.queue * 4 / 96), 0), 4)
