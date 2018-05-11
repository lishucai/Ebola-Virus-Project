import numpy as np
import cv2

'''
The following program processes a CSV file and outputs one float values.
The CSV file should hold temp values and should not be empty. 
The program trasfers the CSV file into a double list and then processes the information in the list. 
Overall it finds the head of the person in the csv file and averages the temperatures that belong to the head. 
the directory should hold the csv files that you want to process   
'''
from os import listdir  # to get all files in a directory
from os.path import isfile, join
import os
import sys
# import matplotlib.pyplot as plt
import csv

good_range = list()

#This function is used to correct the values in the CSV file. It finds the minimum values in
# the double list and substruct it from all the values in the list. This is done to help with the calibration
#of the camera.

def correcting_values(temperatureData):
    #setting intitial values so everythign would be smaller
    min_value = 1000
    #goes through the list to fin the absolute minimum
    for elements in temperatureData:
        temp_min_value = min(elements)
        if temp_min_value < min_value:
            min_value = temp_min_value
    # min_value = min(temperatureData)
    # if DEBUG:
    #    print min_value

    #substruct the minimum value from all values
    for row_counter, elements in enumerate(temperatureData):
        for column_counter, element in enumerate(elements):
            element = element - min_value
            temperatureData[row_counter][column_counter] = element
            # [float(i)-min_value for i in elements]
            # print temperatureData[row][column]

    #returns the new list with changed values
    return temperatureData



#The following funciton finds the point where the head begings. It does that be looking throught the array until it
#finds five values in a row that are in the right range (30-45) then it returns a list with two variables [y,x]
# y is the row where the ead begins and x is the column. If it doesn't find the head it returns an empty list
def starting_point(temperatureData):
    #going over the rows
    for row_counter, elements in enumerate(temperatureData):
        #going over the columns
        for column_counter, element in enumerate(elements):
            if element < 45 and element > 30:
                good = []
                #after finding 1 value looking for the next four
                for iterator in range(1, 5):
                    # print len(elements)
                    if (column_counter + iterator) < len(elements):
                        if elements[column_counter + iterator] < 45 and elements[column_counter + iterator] > 30:
                            # print "added to good"
                            good.append(iterator)
                # print len(good)
                #if it found 5 in a row
                if len(good) == 4:
                    # print "in"
                    cordinates = []
                    cordinates.append(row_counter)
                    cordinates.append(column_counter)
                    return cordinates
    return []

#this function does the same as the previous just with a differernt range in case the file is bad.
def starting_point_bad_file(temperatureData):
    for row_counter, elements in enumerate(temperatureData):
        for column_counter, element in enumerate(elements):
            if element < 50 and element > 30:
                good = []
                for iterator in range(1, 5):
                    # print len(elements)
                    if (column_counter + iterator) < len(elements):
                        if elements[column_counter + iterator] < 50 and elements[column_counter + iterator] > 30:
                            # print "added to good"
                            good.append(iterator)
                # print len(good)
                if len(good) == 4:
                    # print "in"
                    cordinates = []
                    cordinates.append(row_counter)
                    cordinates.append(column_counter)
                    return cordinates
    return []

#This function returns the mean of the head values.
#It recieves the following:
# X and Y the values from the starting point function
#WIDTH AND HEIGHT - variable that are hard coded from absorbing the images. If the person is about 2 meters from
#the camera the head in the picture is about 40 columns wide and 30 rows long
#temperatureData is the array with the temperature values

def get_mean(x, y, WIDTH, HEIGHT, temperatureData):
    #if the head of the person is too law (usually means the image is bad we output an error and
    #returning a 0 for the mean.
    if ((y + HEIGHT) > 120 or ((x + (WIDTH / 2)) > 160)):
        print "PERSON OUT OF RANGE"
        return 0
    #if ((x + (WIDTH / 2)) > 160):
    #    print "PERSON OUT OF RANGE"
    #    return 0
    #going through all the values in the head
    for row in range(y, (y + HEIGHT)):
        # y is the row it begains, h is the width of the length of the head
        for column in range(x - (WIDTH / 2), x + (WIDTH / 2)):
            if (temperatureData[row][column] > 43 or temperatureData[row][column] < 35):
                continue
            else:
                good_range.append(temperatureData[row][column])
    #if the image was bad the langth of the array might be zero. We check it here and return 0 as the mean
    #if that happens.
    if (len(good_range) == 0):
        return 0
    #calculating the mean of all the good values
    range_mean = sum(good_range) / float(len(good_range))
    return range_mean

#this function does the same as the previous just with a differernt range in case the file is bad.
def get_mean_bad_file(x, y, WIDTH, HEIGHT, temperatureData):
    for row in range(y, (y + HEIGHT)):
        # y is the row it begains, h is the width of the length of the head
        for column in range(x - (WIDTH / 2), x + (WIDTH / 2)):
            if (temperatureData[row][column] > 50 or temperatureData[row][column] < 30):
                continue
            else:
                good_range.append(temperatureData[row][column])

    range_mean = sum(good_range) / float(len(good_range))
    return range_mean


# MYPATH = 'C:\Users\Tair\Documents\Pictures\Real\Running'
# MYPATH = 'nfs/stak/users/maimonc/Ebola-Virus-Project/Code/Image_processing\Real\Running'
# MYPATH = './Real/resting'

def processImages():
    #MYPATH - the directory that holds the CSV FILES
    MYPATH = "./Images"
    FILES_NUM = 0
    # we hard coded the size of the head in the image. If the person is about 2 meter from the camera its about 30
    # rows long and about 40 columns wide. You should change these values if you think the head is in a different
    # size in you images.
    HEIGHT = 30
    WIDTH = 40
    # set DEBUG to 1 to use specific DEBUG functionalities. It will have more print statments and will not print a
    DEBUG = 0
    # set this variable to 1. I set it to 0 when we took some images that we'rent in the right range. It increases the range when selecting
    # the head pixels. See  starting_point_bad_file() get_mean_bad_file
    FILE_IS_GOOD = 1
    #setting all nessesery parameters. x and y will hold the point where the head begins
    y = 0
    x = 0
    csv_list = []
    tiff_list = []
    invalid_file_type = []
    # getting the names of all the files in a directory
    getfiles = [f for f in listdir(MYPATH) if
                isfile(join(MYPATH, f))]  # a list of all the file in a folder specified by MYPATH
    # a loop that goes through all the csv file. It will process each csv file by itself.
    for f in getfiles:
        if (f.endswith(".tiff")):  # Add more if statements as necessary for more file types
            tiff_list.append(f)
        elif (f.endswith(".csv")):
            csv_list.append(f)
        else:
            invalid_file_type.append(f)

    print "IMAGES PROCESSED"
    print csv_list

    temperatureMeans = list()
    #turn the CSV file into an array
    for c in csv_list:
        # print c
        temp_file = join(MYPATH, c)  # getting the file with the path, file name is in c
        temperatureData = list()
        tempList = []
        with open(temp_file, 'rb') as f:
            data = csv.reader(f, delimiter=',')
            for row in data:
                tempList = []
                for temp in row:
                    if (temp == '\n'):
                        pass
                    else:
                        tempList.append(float(temp))
                temperatureData.append(tempList)
        #"correcting" (subtructing the minimum) all the values in the array
        temperatureData = correcting_values(temperatureData)
        # print(len(temperatureData))
        # print(len(temperatureData[0]))
        # print len(temperatureData[0])
        good_range = []

        # y = 15
        # x = 75
        cordinates = []
        #seeting the starting point of the head
        #returns empty list if bad file
        cordinates = starting_point(temperatureData)
        #checking that the cordinates ar good
        if not cordinates:
            print "ERROR! NO VALID DATA. CAN NOT FIND PERSON"
            return [0]

        if DEBUG:
            print 'row number is %d, column number is %d ' % (cordinates[0], cordinates[1])

        y = cordinates[0]
        x = cordinates[1]

        #if nothing failed we get the mean of the head from the array.
        if FILE_IS_GOOD:
            temperatureMeans.append(get_mean(x, y, WIDTH, HEIGHT, temperatureData))
    #returns a list of means
    return temperatureMeans


'''		
	    else:
		range_mean = get_mean_bad_file(  x,y,WIDTH, HEIGHT, temperatureData)
'''

'''
	    if DEBUG:
		print 'mean: %f range_mean %s' % (range_mean, c)
	    else:
	       with open('resting.csv', 'a') as file:
		     file.write(str(range_mean))
		     file.write('\n')
		#print '%0.2f %s' %(range_mean, c)
	    return temeratureMeans	
'''
