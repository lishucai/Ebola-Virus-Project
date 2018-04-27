import os
import sys

def reader(fileName):
	masterList = list()
	with open(fileName, 'r') as f:
		lines = f.read().splitlines()
		for pair in lines:
			dataPoint = (float(pair.split()[0]), float(pair.split()[1]))
			masterList.append(dataPoint)
	return masterList

