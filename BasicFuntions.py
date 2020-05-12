import cv2
import numpy as np

img = cv2.imread("Resources\lena.png")

#cvtcolor funtion basically converts an image into diff color
img_gray  = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray Image" , img_gray)
cv2.waitKey(0)

#    GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType]]]) -> dst       
#    .   @brief Blurs an image using a Gaussian filter.
#    .
#    .   The function convolves the source image with the specified Gaussian kernel. In-place filtering is
img_blur = cv2.GaussianBlur(img_gray , (7,7) ,0)
cv2.imshow("Blur image" , img_blur)
cv2.waitKey(0)

# Canny(image, threshold1, threshold2[, edges[, apertureSize[, L2gradient]]]) -> edges
#    .   @brief Finds edges in an image using the Canny algorithm @cite Canny86 . 
#    .
#    .   The function finds edges in the input image and marks them in the output map edges using the
img_canny = cv2.Canny(img_gray, 70,70)
cv2.imshow("Canny Image" , img_canny)
cv2.waitKey(0)

# dilate(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) -> dst
#    .   @brief Dilates an image by using a specific structuring element.
#    .
#    .   The function dilates the source image using the specified structuring element that determines the
grid_matrix = np.ones((5,5) , dtype=np.uint8)
# this add grids at the edges of the canny image
img_dailation = cv2.dilate(img_canny,grid_matrix,iterations=1 ) 
cv2.imshow("Dailation Image" , img_dailation)
cv2.waitKey(0)

#    erode(src, kernel[, dst[, anchor[, iterations[, borderType[, borderValue]]]]]) -> dst
#   .   @brief Erodes an image by using a specific structuring element.
#    .   
#    .   The function erodes the source image using the specified structuring element that determines the
#    .   shape of a pixel neighborhood over which the minimum is taken:
img_eroded = cv2.erode(img_dailation, grid_matrix,iterations=1 ) 
cv2.imshow("Eroded Image" , img_eroded)
cv2.waitKey(0)