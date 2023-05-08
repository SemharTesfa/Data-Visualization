from GraphPy import Graph
import matplotlib.pyplot as plt; plt.rcdefaults()

class BackEnd:
    def __init__(self,data):
        self.graphOb = Graph(data)

    def draw_graph(self, graph):
        if graph == "xy_plot":
            plt = self.graphOb.create_xy_plot()
            plt.show()

        elif graph == "bar_chart":
            plt = self.graphOb.create_bar_chart()
            plt.show()

        elif graph == "linear_regression":
            plt = self.graphOb.create_linear_regression()
            plt.show()


#x = BackEnd("Temperature.html")
#x.draw_graph('bar_chart')

