import csv
import json

class CustomLog():

    def initCollectStress(self):
        with open('results/workers_stress.csv', 'w', newline='') as f:
            outPut = []
            outPut.append(['time', 'worker_id', 'stress'])
            writer = csv.writer(f)
            writer.writerows(outPut)

    def collectStress(self, time, worker_id, stress):
        with open('results/workers_stress.csv', 'a', newline='') as f:
            outPut = []
            outPut.append([time, worker_id, stress])
            writer = csv.writer(f)
            writer.writerows(outPut)
