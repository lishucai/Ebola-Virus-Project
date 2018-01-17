import numpy as np
import cv2
#img = cv2.imread(r'''C:\Users\Tair\Documents\pictures\test.tiff''', cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)


list = [1,2,3,4,5,4,3,4,3,4,12, 14, 5, 1, 5]
good_range = []
for element in list:
    if (element < 2 or element > 10):
        continue
    else:
        good_range.append(element)

range_mean = np.mean(good_range)
range_max = np.max(good_range)
range_min = np.min(good_range)
range_median = np.median(good_range)
range_st_deviation = np.std(good_range)



print(good_range)
print(range_mean)

print "mean: %.2f, max: %.2f, min: %.2f, median: %.2f, standard deviation: %.2f " % (range_mean, range_max, range_min, range_median, range_st_deviation)
