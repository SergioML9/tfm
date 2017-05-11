import datetime

time_by_step = 1800 # seg/step
working_day = 8 # hours

workersTiming = {'arrivalTime' : datetime.time(9, 00), 'leavingTime' : datetime.time(17, 00)}

task_times = [30, 60, 120, 240] # minutes dedicated to the task
task_probs = [0.533, 0.267, 0.133, 0.067] # probs of task with that time
