import cv2
import numpy as np 

img = cv2.imread("Resources\lena.png")
print("Size of the image is :")
print(np.shape(img))
cv2.imshow("Original Image" ,img)
width , height ,_= np.shape(img)
##--or
#width ,height = img.size

#-----------------for twice the size
alimg = cv2.resize(img , (2*width ,2*height))
cv2.imshow("Twice The size" , alimg)
cv2.waitKey(10000)

alimg = cv2.resize(img , (width//2 ,height//2))
cv2.imshow("Half The size" , alimg)
cv2.waitKey(10000)

alimg = cv2.resize(img , (640,480))
cv2.imshow("640x480" , alimg)
cv2.waitKey(10000)

if cv2.waitKey(100000) & 0xFF == ord('q') :
    cv2.destroyAllWindows()

cv2.imshow("original Image" , img)

#   This means height from 200 to 500 and width from 300 to 400.
cropimg = img[200:500 , 200:480]

cv2.imshow("Croped img" , cropimg)
cv2.waitKey(0)

if cv2.waitKey(100000) & 0xFF == ord('q') :
    cv2.destroyAllWindows()

