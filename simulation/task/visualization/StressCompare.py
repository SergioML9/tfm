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
        if model.time.new_day:
            stress = [model.users[0].stress, model.users[1].stress]
            model.time.new_day = False
            return [stress, "Day " + str(model.time.days)]
        else:
            return -1
