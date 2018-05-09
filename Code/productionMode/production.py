import sys
import csv
import os

import images2
import LeastSquares
import reader

import numpy as np
import cv2
from ir_cam import IrCamera

def mean(values):
	return float(sum(values)) / max(len(values), 1)

def modelPredict(rawTemp, modelDataName):
	modelData = reader.commaReader(modelDataName)
	predictedTemp = (rawTemp * float(modelData[0])) + float(modelData[1])

	return predictedTemp

def takeThermalImage(configFile):
	path = "./Images"
	name = "image" 
	with IrCamera(configFile) as ir_cam:

	    for i in range(40):
		data_t, data_p = ir_cam.get_frame()
		cv2.imshow('visual data', data_p)
		print '----------------'
		print data_t
		print '----------------'
		cv2.waitKey(5)
	    
		n_rows, n_cols = data_t.shape
	    #print data_t[0]

		if(i > 10):
			filename = str(name + str(i) + ".csv")
			with open(os.path.join(path, filename), 'w') as csvfile:
				thermalwriter = csv.writer(csvfile)
				for row in range(n_rows):
					thermalwriter.writerow(data_t[row])   

if __name__ == "__main__":
	if(len(sys.argv) == 1):
		print "Usage"
		print "Create Model: python production.py -c <trainingData.txt>"
		print "Take Image: python production.py config.xml <modelFile.txt>"
	
	elif(sys.argv[1] == "-c"):
		trainingData = reader.spaceReader(sys.argv[2])
		LeastSquares.generateModel(trainingData)
	else:
		#The config files for the camera and the model.
		config = sys.argv[1]
		modelData = sys.argv[2]

		#Taking the image using the first config file.
		takeThermalImage(config)
		
		#Getting the means of all the files.
		imageMeans = images2.processImages()

		if(0 in imageMeans):
			print "An error has occured. Try again."	
		else:
			#Getting the mean of all the means
			totalMean = mean(imageMeans)

			#Running the total mean through the model.
			print "Raw Processed Temperature: ", totalMean
			print "Predicted Core Body Temperature: " ,modelPredict(totalMean, modelData)

			print "DONE"

