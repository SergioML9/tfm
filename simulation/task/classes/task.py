import random
import configuration.settings

class Task():

    def __init__(self):

        random_prob = random.random()

        if random_prob < configuration.settings.task_probs[0]:
            self.time = configuration.settings.task_times[0]
        elif random_prob > configuration.settings.task_probs[0] and random_prob < (configuration.settings.task_probs[0] + configuration.settings.task_probs[1]):
            self.time = configuration.settings.task_times[1]
        elif random_prob > (configuration.settings.task_probs[0] + configuration.settings.task_probs[1]) and random_prob < (configuration.settings.task_probs[0] + configuration.settings.task_probs[1] + configuration.settings.task_probs[2]):
            self.time = configuration.settings.task_times[2]
        else:
            self.time = configuration.settings.task_times[3]
