import datetime

time_by_step = 60 # seg/step
working_day = 8 # hours

workersTiming = {'arrivalTime' : datetime.time(9, 00), 'leavingTime' : datetime.time(17, 00), 'overtimeLimit' : datetime.time(19, 00) , 'sleepStart' : datetime.time(00, 00), 'sleepEnd' : datetime.time(7, 00)}

# distributions params
unlimited_email = 4.70, 4.1 #12.54, 8.02 or 4.70 4.1
emails_read_distribution_params = unlimited_email

email_time_reception_distribution_params = 92, 1.5 # http://www.radicati.com/wp/wp-content/uploads/2015/02/Email-Statistics-Report-2015-2019-Executive-Summary.pdf
email_read_time_distribution_params = 23, 3 # TODO: search for real values

tasks_arriving = 20, 6
tasks_arriving_distribution_params = tasks_arriving
tasks_estimated_length = [25, 25] # TODO: search for real values
tasks_probs = [0.67, 0.33] # TODO: search for real values

fatigue_tolerance = 1, 0.1
fatigue_tolerance_distribution_paramas = fatigue_tolerance
