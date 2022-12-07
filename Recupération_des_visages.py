# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 13:36:05 2022

@author: Ulrich_Lumendo
"""

import pickle
import cv2
import os



#find path of xml file containing haarcascade file
cascPathface = os.path.dirname(
 cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
# load the harcaascade in the cascade classifier
faceCascade = cv2.CascadeClassifier(cascPathface)
# load the known faces and embeddings saved in last file
data = pickle.loads(open('face_enc', "rb").read())
#Find path to the image you want to detect face and pass it here
image = cv2.imread("Ulcard.jpg")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#convert image to Greyscale for haarcascade
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(gray,
                                     scaleFactor=1.1,
                                     minNeighbors=5,
                                     minSize=(60, 60),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
print("Il y a {0} visages(s).".format(len(faces)))

for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
for i in range(len(faces)):
    print("Cadre du visage n° {0} --> {1} ".format(i+1, faces[i]))
for i in range(len(faces)) :
    crop_img = image[faces[i][1]:faces[i][1]+faces[i][3], faces[i][0] :faces[i][0]+faces[i][2]]
    cv2.imwrite('C:/Users/user/Face_recognition/image_card' +str(i) + '.jpg', crop_img)
cv2.imshow('Le resultat', crop_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

