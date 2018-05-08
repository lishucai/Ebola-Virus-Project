import numpy as np
import cv2
from os import listdir  # to get all files in a directory
from os.path import isfile, join
import os
import sys

#import matplotlib.pyplot as plt
import csv

def correcting_values(temperatureData):

    min_value = 1000
    max_value = 0
    for elements in temperatureData:
        temp_min_value = min(elements)
        temp_max_value = max(elements)
        if temp_min_value < min_value:
            min_value = temp_min_value
        if temp_max_value > max_value:
            max_value = temp_max_value
    print 'max: %f ' % (max_value)
    print 'min: %f ' % (min_value)


    #min_value = min(temperatureData)
    if DEBUG:
        print min_value
    for row_counter, elements in enumerate(temperatureData):
        for column_counter, element in enumerate(elements):
            element = element - min_value
            temperatureData[row_counter][column_counter] = element
            #[float(i)-min_value for i in elements]
            #print temperatureData[row][column]

    return temperatureData



def starting_point(temperatureData):
    for row_counter, elements in enumerate(temperatureData):
        for column_counter, element in enumerate(elements):
            if element < 45 and element > 30:
                good = []
                for iterator in range(1, 5):
                    # print len(elements)
                    if (column_counter + iterator) < len(elements):
                        if elements[column_counter + iterator] < 45 and elements[column_counter + iterator] > 30:
                            # print "added to good"
                            good.append(iterator)
                #print len(good)
                if len(good) == 4:
                    # print "in"
                    cordinates = []
                    cordinates.append(row_counter)
                    cordinates.append(column_counter)
                    return cordinates
    return []

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
                #print len(good)
                if len(good) == 4:
                    # print "in"
                    cordinates = []
                    cordinates.append(row_counter)
                    cordinates.append(column_counter)
                    return cordinates
    return []


def get_mean(x, y, WIDTH, HIGHT, temperatureData):
    for row in range(y, (y + HIGHT)):
        # y is the row it begains, h is the width of the length of the head
        for column in range(x - (WIDTH / 2), x + (WIDTH / 2)):
            if (temperatureData[row][column] > 43 or temperatureData[row][column] < 35):
                continue
            else:
                good_range.append(temperatureData[row][column])
    if (len(good_range) > 0):
        range_mean = sum(good_range) / float(len(good_range))
        return range_mean
    else:
        return 0

def get_mean_bad_file(x, y, WIDTH, HIGHT, temperatureData):
    for row in range(y, (y + HIGHT)):
        # y is the row it begains, h is the width of the length of the head
        for column in range(x - (WIDTH / 2), x + (WIDTH / 2)):
            if (temperatureData[row][column] > 50 or temperatureData[row][column] < 30):
                continue
            else:
                good_range.append(temperatureData[row][column])

    range_mean = sum(good_range) / float(len(good_range))
    return range_mean

if __name__ == '__main__':

    MYPATH = 'C:\Users\Tair\Documents\Pictures\Files_bill'
    FILES_NUM = 0
    HIGHT = 30
    WIDTH = 40
    DEBUG = 0
    FILE_IS_GOOD = 1
    y = 0
    x = 0
    csv_list = []
    tiff_list = []
    invalid_file_type = []
    # getting the names of all the files in a directory
    getfiles = [f for f in listdir(MYPATH) if
                isfile(join(MYPATH, f))]  # a list of all the file in a folder specified by MYPATH

    for f in getfiles:
        if (f.endswith(".tiff")):  # Add more if statements as necessary for more file types
            tiff_list.append(f)
        elif (f.endswith(".csv")):
            csv_list.append(f)
        else:
            invalid_file_type.append(f)

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
        temperatureData = correcting_values(temperatureData)

        # print len(temperatureData[0])
        good_range = []

        # y = 15
        # x = 75
        cordinates = []
        cordinates = starting_point(temperatureData)
        if not cordinates:
            print "error! list of cordinates is empty"

        if DEBUG:
            print 'row number is %d, column number is %d ' %(cordinates[0], cordinates[1])

        y = cordinates[0]
        x = cordinates[1]

        if FILE_IS_GOOD:
            range_mean = get_mean(x,y,WIDTH, HIGHT, temperatureData)
        else:
            range_mean = get_mean_bad_file(  x,y,WIDTH, HIGHT, temperatureData)



        if DEBUG:
            print 'mean: %f range_mean %s' % (range_mean, c)
        else:
            print '%0.2f %s' %(range_mean, c)


