from mesa.visualization.ModularVisualization import VisualizationElement
import numpy as np

class StressCompare(VisualizationElement):
    package_includes = ["Chart.min.js"]
    local_includes = ["visualization/StressCompare.js"]

    def __init__(self, canvas_height, canvas_width):
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        new_element = "new StressCompare({}, {})"
        new_element = new_element.format(canvas_width,
                                         canvas_height)
        self.js_code = "elements.push(" + new_element + ");"

    def render(self, model):
        #wealth_vals = [agent.stress for agent in model.users]
        #hist = np.histogram(wealth_vals, bins=self.bins)[0]
        if model.new_day:
            total_event_stress = sum(user.event_stress for user in model.workers)
            total_effective_fatigue = sum(user.effective_fatigue for user in model.workers)
            total_time_pressure = sum(user.time_pressure for user in model.workers)
            #model.time.new_day = False
            return [[total_event_stress/len(model.workers), total_effective_fatigue/len(model.workers), total_time_pressure/len(model.workers)], "Day " + str(model.time.days + 1)]
        else:
            return -1
