import cv2
import numpy as np

image = np.zeros((512, 512, 3), np.uint8)
cv2.line(image, (0,0), (512,512),(0,255,0),3)
cv2.rectangle(image, (50,50), (200, 100), (0,0,255),2)
cv2.circle(image, (256,256),100,(255,255,255),2)
cv2.putText(image, "hello", (0,200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)
cv2.namedWindow('image')
cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
