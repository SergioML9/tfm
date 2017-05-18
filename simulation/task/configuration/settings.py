import datetime

time_by_step = 1800 # seg/step
working_day = 8 # hours
real_max_stress =  12
max_stress = 6

workersTiming = {'arrivalTime' : datetime.time(9, 00), 'leavingTime' : datetime.time(17, 00)}

task_times = [30, 60, 120, 180] # minutes dedicated to the task
task_probs = [0.4, 0.333, 0.200, 0.067] # probs of task with that time

productivity_probs = [0.15, 0.075, 0.01] # probs of be more efficient at work (duplicate capacity)

new_email_prob = 0.05 # prob of receiving a new email
email_with_task_prob = 0.01 # prob of an email to contain a task

automate_task_prob = 0.15 # prob of automate a task

unlimited_email = 12.54, 8.02
emails_read_distribution_params = unlimited_email
