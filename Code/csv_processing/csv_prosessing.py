import os
import sys
import numpy
import matplotlib.pyplot as plt
import csv

temperatureData = list()
with open(sys.argv[1], 'rb') as f:
    data = csv.reader(f, delimiter=';')
    for row in data:
        for temp in row:
            if(temp == ''):
                pass
            else:
                temperatureData.append(float(temp))


plt.hist(temperatureData)
plt.title("Temperature Histogram")
plt.xlabel("Temp in C")
plt.ylabel("Frequency")
plt.show()
