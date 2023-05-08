"""
Graph.py
* Use MatPlotLib to create the selected graph or chart
* Design a Graph class which manages the MatPlotLib operations. 
 See the MatPlotLib examples.  For example write class member
  functions to draw a Plot, Bar and Linear Regression.
"""
from AnnualTemperature import AnnualTemperature
from sklearn.linear_model import LinearRegression
from pandas import DataFrame
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np

class Graph:
    def __init__(self, data):
        self.T = AnnualTemperature()
        self.data = self.T.getData(data)

    def create_xy_plot(self):
        data = self.data
        keys = data.keys()
        values = [data[key] for key in keys]
        plt.plot(keys, values)

        plt.xlabel('Year')
        plt.ylabel('Temperature in °C')
        plt.title('Average Temperature Annually, Global')
        return plt
        

    def create_bar_chart(self):
        data = self.data
        keys = data.keys()
        values = [data[key] for key in keys]
        plt.bar(keys, values)
        
        plt.xlabel('Year')
        plt.ylabel('Temperature in °C')
        plt.title('Average Temperature Annually, Global')
        return plt

    def create_bar_chart1(self):
        data = self.data
        keys = data.keys()
        values = [data[key] for key in keys]

        y_pos = np.arange(len(keys))

        plt.bar(y_pos, values, align='center', alpha=0.5)
        plt.xticks(y_pos, keys)
        plt.xlabel('Year')
        plt.ylabel('Temperature in °C')
        plt.title('Average Temperature Annually, Global')

        return plt

    def create_linear_regression(self):
        data = self.data
        keys = data.keys()
        values = [data[key] for key in keys]

        X = DataFrame(keys).values.reshape(-1, 1)
        Y = DataFrame(values).values.reshape(-1, 1)

        linear_regressor = LinearRegression()  # create object for the class
        linear_regressor.fit(X, Y)  # perform linear regression
        Y_pred = linear_regressor.predict(X)  # make predictions
        plt.scatter(X, Y)
        plt.plot(X, Y_pred, color='red')
        plt.xlabel('Year')
        plt.ylabel('Temperature in °C')
        plt.title('Average Temperature Annually, Global')
        
        return plt
        
#x = Graph("Temperature.html")
#x.create_xy_plot()
#x.create_bar_chart()
#x.create_linear_regression()
#plt.show()







