import cv2
import numpy as np

width, height = 250, 350
img = cv2.imread('cards.jpg')
pts1 = np.float32([[113,222], [285,191], [159,478], [349,434]])
pts2 = np.float32([[0,0],[width,0], [0,height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_result = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow('image', img)
cv2.imshow('result', img_result)
cv2.waitKey(0)
cv2.destroyAllWindows()