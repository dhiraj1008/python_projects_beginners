#even after downloading opencv if u found module not found then  u need to type in terminal
#pip install opencv-python  opencv-python-headless

import cv2

# this is to include the .xml file into the our code,which helps to detect the face easily
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# import the image into our application
img = cv2.imread('fdect2.jpg')

# and to read the image ,here image need to be in gray color so convert it.
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detect the faces
faces = face_cascade.detectMultiScale(gray,1.1,4)

# draw rectangle to that face

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

# display the result
cv2.imshow('img',img)

# wait to entre the key
cv2.waitKey()

# save the image
cv2.imwrite("fd.jpg",img)

