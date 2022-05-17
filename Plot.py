from msilib.schema import Class
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

class Plot :

    def __init__(self,data):
        self.data = data

    def new(self):

        plt.figure(num=1)
        plt.ion()
        plt.style.use('ggplot')
        plt.plot(self.data.time, self.data.temp, 'ro-')
        plt.ylabel("temperature")
        plt.xlabel("time")
        plt.ylim(min(self.data.temp),max(self.data.temp))
        plt.grid(True)

        plt.pause(0.001)
        plt.show()
        plt.savefig('temp.png')

        plt.figure(num=2)
        plt.ion()
        plt.style.use('ggplot')
        plt.plot(self.data.time, self.data.CO2, 'go-')
        plt.ylabel("CO2")
        plt.xlabel("time")
        plt.grid(True)

        plt.pause(0.001)
        plt.show()
        plt.savefig('CO2.png')

        plt.figure(num=3)
        plt.ion()
        plt.style.use('ggplot')
        plt.plot(self.data.time, self.data.humidity, 'bo-')
        plt.ylabel("humidity")
        plt.xlabel("time")
        plt.ylim(min(self.data.humidity),max(self.data.humidity))
        plt.grid(True)

        plt.pause(0.001)
        plt.show()
        plt.savefig('humidity.png')



