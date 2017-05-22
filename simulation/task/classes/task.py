import random
import configuration.settings

class Task():

    def __init__(self):

        random_prob = random.random()

        if random_prob < configuration.settings.tasks_probs[0]:
            self.time = configuration.settings.tasks_estimated_length[0]
        elif random_prob > configuration.settings.tasks_probs[0] and random_prob < (configuration.settings.tasks_probs[0] + configuration.settings.tasks_probs[1]):
            self.time = configuration.settings.tasks_estimated_length[1]
