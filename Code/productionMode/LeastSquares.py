import os
import sys
import math
import reader
import numpy
import matplotlib.pyplot as plt

def generateModel(pointsList):
	#initializing variables
	xSum = 0
	xSquareSum = 0
	ySum = 0
	ySquareSum = 0
	mulSum = 0
	numerator = 0
	denominator = 0
	slope = 0
	intercept = 0

	xpoints = list()
	ypoints = list()

	#calculating slope
	for point in pointsList:
		mulSum += (point[0] * point[1])
		xSum += point[0]
		xSquareSum += (point[0] * point[0])
		ySum += point[1]
		ySquareSum += (point[1] * point[1])
		xpoints.append(point[0])
		ypoints.append(point[1])

	numerator = mulSum - ((xSum * ySum)/len(pointsList))
	denominator = xSquareSum - (pow(xSum, 2)/len(pointsList))
	#print(numerator)
	#print(denominator)
	slope = float(numerator)/float(denominator)

	#calculating intercept
	intercept = (ySum - (slope * xSum))/len(pointsList)
	
	#calculating R^2
	rNumerator = (len(pointsList) * float(mulSum)) - ((float(xSum) * float(ySum)))
	rDenominator = math.sqrt(((len(pointsList) * xSquareSum) - (xSum * xSum)) * ((len(pointsList) * ySquareSum) - (ySum * ySum)))
	r = rNumerator/rDenominator
	rsquare = (r * r)
	#print "r^2:",rsquare 

	#creating a linear line for the graph
	x = numpy.linspace(35,38,50)
	y = (slope * x) + intercept

	#Creating the scatter plot
	#plt.scatter(xpoints, ypoints)
	#plt.xlabel("Camera Temperatures")
	#plt.ylabel("Thermometer Temperatures")
	#plt.plot(x,y)
	#plt.show()
		
	with open("model.txt", 'w') as modelFile:
		modelFile.write(str(slope))
		modelFile.write(',')
		modelFile.write(str(intercept))

