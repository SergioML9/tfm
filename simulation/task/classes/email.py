import random
import configuration.settings

class Email():

    def __init__(self):

        self.contains_task = False
        if random.random() < configuration.settings.email_with_task_prob:
            self.contains_task = True
