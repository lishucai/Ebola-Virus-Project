# CS 463 CAPSTONE

## Ebola Project Group CS34

## Background

In the medical industry it is known that one of the first signs of illness is an elevated core body temperature. Currently, the only way to get this temperature is with contact sensors which put health care workers at risk of infection if a patient is ill. This project will aim to help solving this problem by creating a device that will be able to quickly take a person's core body temperature from a distance using only stand-off sensors.


## Description:

Our final program (under code/productionMode) first connects to a thermal camera and takes a few pictures. Then, it transfers these images into CSV files that hold each pixels temperature (in Celsius). After that our code process those CSV files, produces a mean temperature value of the person in the image and send that value into a mathematical model. It will then interpret the data to create a mathematical model that uses the temperature of a	person's skin as data and analyzes that information and predicts what their core body temperature is.
