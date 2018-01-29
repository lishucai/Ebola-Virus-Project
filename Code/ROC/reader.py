import os
import sys

def readData(fileName):
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
    return (measuredTemp, realTemp, correctness)

