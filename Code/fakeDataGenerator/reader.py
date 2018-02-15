import os
import sys

fileName = sys.argv[1]
measuredTemp = list()
realTemp = list()
correctness = list()
with open(fileName, 'r') as f:
    lines = f.read().splitlines()
    for tempData in lines:
        tp = tempData.split(',')
        measuredTemp.append(tp[0])
        realTemp.append(tp[1])
        correctness.append(tp[2])


f.close()
print(measuredTemp)
print(realTemp)
print(correctness)
