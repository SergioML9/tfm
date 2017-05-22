from mesa.visualization.ModularVisualization import VisualizationElement
import numpy as np

class AccumulatedTasks(VisualizationElement):
    package_includes = ["Chart.min.js"]
    local_includes = ["visualization/AccumulatedTasks.js"]

    def __init__(self, canvas_height, canvas_width):
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        new_element = "new AccumulatedTasks({}, {})"
        new_element = new_element.format(canvas_width,
                                         canvas_height)
        self.js_code = "elements.push(" + new_element + ");"

    def render(self, model):
        #wealth_vals = [agent.stress for agent in model.users]
        #hist = np.histogram(wealth_vals, bins=self.bins)[0]
        if model.time.hours == 20 and model.time.minutes == 0:
            total_acumulated = sum(len(user.tasks) for user in model.workers)
            #model.time.new_day = False
            return [total_acumulated/len(model.workers), "Day " + str(model.time.days + 1)]
        else:
            return -1
