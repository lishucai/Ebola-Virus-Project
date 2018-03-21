#!/usr/bin/python
from numpy import array, newaxis
from sklearn import datasets, linear_model

e = []
m = []

with open("trainTemps.txt") as file:
	for line in file:
		temps = line.split()
		e.append(float(temps[0]))
		m.append(float(temps[1]))

est = array(e)
meas = array(m)

est = est[:, newaxis]

lin = linear_model.LinearRegression()

lin.fit(est, meas)

print("The coefficient is {}".format(lin.coef_[0]))
print("The intercept is {}".format(lin.intercept_))

x = []
y = []

with open("testTemps.txt") as file:
	for line in file:
		temps = line.split()
		x.append(float(temps[0]))
		y.append(float(temps[1]))

x = array(x)
y = array(y)

x = x[:, newaxis]

print ("The R squared value is {}".format(lin.score(x, y)))

t = []

with open("temps.txt") as file:
	for line in file:
		temps = line.split()
		t.append(float(temps[0]))

t = array(t)

t = t[newaxis, :]

print ("The predicted temperature is {}".format(lin.predict(t)))
