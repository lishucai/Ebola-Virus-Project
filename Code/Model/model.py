#!/usr/bin/env python

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.gaussian_process import GaussianProcess
from sklearn.cross_validation import cross_val_predict
from numpy import array, newaxis, concatenate


def read_data(filename):
	# Read in the training data, and get rid of the dupes
	with open(filename, 'r') as f:
		data = list(set([tuple(map(float, line.split())) for line in f]))

	thermal = [t for t,c in data]
	core = [c for t,c in data]

	thermal = array(thermal)[:, newaxis]
	core = array(core)

	return thermal, core


def fit_linear_model(thermal, core):
	model = LinearRegression(normalize=True)
	model.fit(thermal, core)

	return model


def fit_gaussian_model(thermal, core):
	model = GaussianProcess()
	model.fit(thermal, core)

	return model


def evaluate(model, thermal, core):
	'''
	Calculate the sum squared error for a predictive model.
	'''
	guess = model.predict(thermal)
	return sum([(a - b) ** 2 for a,b in zip(guess, core)])	


def loocv(model, thermal, core):
	guess = cross_val_predict(model, thermal, core, cv=len(thermal))
	return sum([(a - b) ** 2 for a,b in zip(guess, core)])	


def graph(model, thermal, core):
	'''
	Graph a predictive model.
	'''
	guess = model.predict(thermal)
	plt.scatter(thermal, core, color='black')
	plt.plot(thermal, guess, color='blue', linewidth=3)
	plt.title("Skin Temperature vs. Core Temperatue")
	plt.xlabel("Skin Temperature")
	plt.ylabel("Core Temperature")
	plt.grid()
	plt.show()
	return


if __name__ == '__main__':

	filename = raw_input('Enter the name of the file that contains the data (it must be in the same directory as this program): ')

	thermal, core = read_data(filename)

	print 'Linear:'
	model = fit_linear_model(thermal, core)
	print '    SSE:', evaluate(model, thermal, core)
	print '  LOOCV:', loocv(model, thermal, core)
	graph(model, thermal, core)

	print 'Gaussian:'
	model = fit_gaussian_model(thermal, core)
	print evaluate(model, thermal, core)
	print '    SSE:', evaluate(model, thermal, core)
	print '  LOOCV:', loocv(model, thermal, core)
	graph(model, thermal, core)
