import numpy as np
import cv2

# Load an color image in grayscale
#IMREAD_COLOR = 1
#IMRED_UNCHANGED = -1
#IMREAD_GRAYSCALE = 0

'''
face_cascade = cv2.CascadeClassifier(r'''C:\Users\Tair\Documents\OpenCV\opencv\build\etc\haarcascades\haarcascade_frontalface_default.xml''')
eye_cascade = cv2.CascadeClassifier(r'''C:\Users\Tair\Documents\OpenCV\opencv\build\etc\haarcascades\haarcascade_eye.xml''')
'''

#reading the image, won't return an error if the path is wrong!
#img = cv2.imread(r'''C:\Users\Tair\Documents\pictures\person.jpg''',0)
img = cv2.imread(r'''C:\Users\Tair\Documents\pictures\test.tiff''', cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
#img = cv2.imread(r'''C:\Users\Tair\Documents\pictures\test4.tiff''')
'''
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

print(faces)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#shows the image until you press a keyboard
cv2.imshow('image',img)
cv2.waitKey(1000)
cv2.destroyAllWindows()

#open the image in a new window
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(1000)
cv2.destroyAllWindows()
'''
#getting pixle values

#getting the pixles value of [100,100]
print "getting pixle value for [100,100]"
px = img[100,100]
print(px)

'''
#changing the pixle value of [100,100]
print "after changing pixle vlaue"
img[100,100] =255
print img[100,100]
'''
#prints out the shape of the image
#two values if grey, three if it's in color
print "image shape (y and x)"
print img.shape
#print img.shape[0]
#print img.shape[1]
y = img.shape[0]
x = img.shape[1]
'''
#for loop that goes throu the image and prints every pixle value
sum_pixles = 0 
for i in range (0,259):
    for j in range (0,194):
        px = img[i,j]
        #the scale is of 0 to 255
        if (px > 230 or px < 50):
            sum_pixles += 0
        else:
            sum_pixles = sum_pixles +px
        #print(i)
        #print(j)
        #print(px)        
print "sum of pixles: %d" %sum_pixles
avg = sum_pixles/(y*x)
print "avg of pixles: %d" % avg 
'''

pixel_list = []
#for loop that goes throu the image and prints every pixle value
sum_pixles = 0 
for i in range (0,10):
    for j in range (0,10):
        px = img[i,j] #goes through the image
        temp = [i,j,px[0], px[1], px[2]] #get the three values of each pixle
        #print(temp)
        pixel_list.append(temp) #append the value to the list 
        #print(px)
        #the scale is of 0 to 255
        '''if (px > 230 or px < 50):
            sum_pixles += 0
        else:
            sum_pixles = sum_pixles +px
        
        #print(i)
        #print(j)
        #print(px)        
print "sum of pixles: %d" %sum_pixles
avg = sum_pixles/(y*x)
print "avg of pixles: %d" % avg
'''
print(pixel_list)
