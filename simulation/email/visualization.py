from StressModel import *
from StressAgent import *
import matplotlib.pyplot as plt


model = StressModel(1000)
for i in range(24):
    model.step()

#agent_stress = [a.stres for a in model.schedule.agents]
#plt.hist(agent_wealth)

agent = model.datacollector.get_agent_vars_dataframe()
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

end_stressa = agent.xs(23, level="Step")["Queue"]
end_stressa.hist(bins=range(agent.Queue.max()+1))

plt.show()
