#!/usr/bin/env python


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


if __name__ == '__main__':
	thermal, core = read_data('allTemps.txt')

	print 'Linear:'
	model = fit_linear_model(thermal, core)
	print '    SSE:', evaluate(model, thermal, core)
	print '  LOOCV:', loocv(model, thermal, core)

	print 'Gaussian:'
	model = fit_gaussian_model(thermal, core)
	print evaluate(model, thermal, core)
	print '    SSE:', evaluate(model, thermal, core)
	print '  LOOCV:', loocv(model, thermal, core)
