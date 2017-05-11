from model.stressModel import *
from agents.stressAgent import *
import matplotlib.pyplot as plt
from mesa.visualization.ModularVisualization import ModularServer
from HistogramModule import HistogramModule

histogram = HistogramModule(list(range(100)), 200, 1000)
server = ModularServer(StressModel,
                       [histogram],
                       "Stress Model",
                       5)
server.launch()

#model = StressModel(10)
#for i in range(48):
#    model.step()

#agent_stress = [a.stres for a in model.schedule.agents]
#plt.hist(agent_wealth)

#agent = model.datacollector.get_agent_vars_dataframe()
#one_agent_stress = agent_stress.xs(0, level="AgentID")
#plt.subplot(211)
#one_agent_stress.Stress.plot()

# pinta el número de emails automatizado
#plt.subplot(211)
#one_automated_emails = agent.xs(23, level="AgentID")
#one_automated_emails.AutomatedEmails.plot()

#plt.subplot(212)
#end_stress = agent.xs(23, level="Step")["Stress"]
#end_stress.hist(bins=range(agent.Stress.max()+1))

#plt.show()
