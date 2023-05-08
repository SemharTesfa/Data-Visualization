# AnnualTemperature.py
#* A class to handle the global annual temperature data
from Process import Processor
import re

class AnnualTemperature:
    def __init__(self):
        self.P = Processor()
        self.temperature = {}

    def getData(self, data):
        temperature_read = self.P.readData(data)
        self.temperature = self.P.parseTemperature(temperature_read)
        return self.temperature

    def setDebug(self):
        print(f'Year \t Median')
        print(f'===============')
        for key, val in self.temperature.items():
            print(f'{key} \t {val:<3.3f}')

# Test        
# s = AnnualTemperature()
# s.getData("Temperature.html")
# s.setDebug()

