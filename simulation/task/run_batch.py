from mesa.batchrunner import BatchRunner
from model.stressModel import *
from agents.workerAgent import *
import numpy as np

# The below is needed for both notebooks and scripts
import matplotlib.pyplot as plt

parameters = {"N" : 100}

batch_run = BatchRunner(StressModel,
                        parameters,
                        iterations=1,
                        max_steps=43200,
                        agent_reporters={"Stress": lambda a: a.stress if isinstance(a, WorkerAgent) else None,
                            "Productivity": lambda a: a.productivity if isinstance(a, WorkerAgent) else None})
batch_run.run_all()

run_data = batch_run.get_agent_vars_dataframe()
run_data.hist()
#stress_data = run_data["Stress"]
#plt.subplot(211)
#stress_data.hist(bins=np.arange(0, 1.1, 0.1))
#productivity_data = run_data["Productivity"]
#plt.subplot(212)
#productivity_data.hist(bins=np.arange(0, 1.5, 0.25))
plt.show()
