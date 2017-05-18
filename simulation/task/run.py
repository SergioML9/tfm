from model.stressModel import *
import matplotlib.pyplot as plt
from mesa.visualization.ModularVisualization import ModularServer
from visualization.HistogramModule import HistogramModule
from visualization.AverageStress import AverageStress
from visualization.StressCompare import StressCompare

histogram = HistogramModule(list(range(0, 12)), 200, 1000)
average_stress = AverageStress(200, 1000)
stress_compare = StressCompare(200, 1000)

server = ModularServer(StressModel,
                       [histogram, average_stress, stress_compare],
                       "Stress Model",
                       100)
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
