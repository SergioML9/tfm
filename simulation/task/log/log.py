import csv
import json

class CustomLog():

    def initCollectStress(self):
        with open('results/agents_stress.csv', 'w', newline='') as f:
            outPut = []
            outPut.append(['time', 'agent_id', 'stress'])
            writer = csv.writer(f)
            writer.writerows(outPut)

    def collectStress(self, time, agent_id, stress):
        with open('results/agents_stress.csv', 'a', newline='') as f:
            outPut = []
            outPut.append([time, agent_id, stress])
            writer = csv.writer(f)
            writer.writerows(outPut)
