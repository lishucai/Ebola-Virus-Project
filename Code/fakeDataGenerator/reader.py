import os
import sys

fileName = sys.argv[1]
measuredTemp = list()
realTemp = list()
with open(fileName, 'r') as f:
    lines = f.read().splitlines()
    for tempPair in lines:
        tp = tempPair.split(',')
        measuredTemp.append(tp[0])
        realTemp.append(tp[1])


f.close()
print(measuredTemp)
print(realTemp)
