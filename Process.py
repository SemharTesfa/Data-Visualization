# Process.py
# * Design a set of classes/functions process the data
# * Store the data in the DataBase for both the CO2 and Temperature data.
import matplotlib.pyplot as plt
import re

class Processor:
    def __init__(self):
        self.lines = []
        self.carbon = {}
        self.temperature = {}

    def readData(self, htmlFile):
        with open(htmlFile, 'r') as inFile:
            self.lines = inFile.readlines()
            return self.lines

    def parseCarbon(self, htmlFile):
        yearPattern = r'[0-9]{4}'
        averagePattern = r'\>[0-9]{3}\.[0-9]{2}\<'
        avgList = []      
        for line in self.lines:
            resultYear = re.search(yearPattern, line)
            resultAverage = re.search(averagePattern, line)
            if resultYear and resultAverage:
                year = int(resultYear.group())
                average = float(resultAverage.group()[1:-1])
                self.carbon[year] = average
                if year in self.carbon.keys():
                    avgList.append(average)
                    avg = sum(avgList)/ len(avgList)
                    self.carbon[year] = average            
        return self.carbon

    def parseTemperature(self, htmlFile):
        data_regex = re.compile(r'([0-9]{4})</TD><TD>(-?0\.[0-9]{1,3})')
     
        for line in self.lines:
            result = re.search(data_regex, line)
            if result:
                year = int(result.group(1))
                median = float(result.group(2))
                self.temperature[year] = median
           
        return self.temperature

        
