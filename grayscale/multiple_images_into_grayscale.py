import cv2
import glob
import os

os.mkdir('C:/Users/ELCOT/Desktop/vishwa pycharm assignment/GrayScale_Images')
images_path =glob.glob('C:/Users/ELCOT/Desktop/vishwa pycharm assignment/*.jpg')

i = 0
for image in images_path:
    img = cv2.imread(image)
    gray_images = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Images', gray_images)
    cv2.imwrite('C:/Users/ELCOT/Desktop/vishwa pycharm assignment/GrayScale_Images/image%02i.jpg' %i, gray_images)
    i += 1
    cv2.waitKey(600)
    cv2.destroyAllWindows()